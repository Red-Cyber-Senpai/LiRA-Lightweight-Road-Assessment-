"""
LiRA (Light-weight Road Assessment) - Web Interface
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Date: April 10, 2026
Description: Flask-based API for receiving and monitoring road condition sensor data.
Copyright (c) 2026 Saketcharan Chauhan M & Abubakr Siddiq Mohammed. All rights reserved.
"""

import threading
import time
import yaml
from flask import Flask, request, jsonify

# LiRA Custom Modules
from detection_logic import RoadDetectionEngine
from gps_handler import GPSHandler
import dataprocessing

# Load Configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initialize Engines
detection_cfg = config['detection']
engine = RoadDetectionEngine(
    pothole_threshold=detection_cfg['pothole_variance_threshold'],
    smooth_threshold=detection_cfg['smooth_variance_threshold'],
    window_size=detection_cfg['window_size']
)
gps = GPSHandler()

app = Flask(__name__)
sensor_data = []

@app.route('/data', methods=['POST'])
def receive_sensor_data():
    global sensor_data
    try:
        data = request.json
        if data:
            sensor_data.append(data)
            return jsonify({"status": "success", "message": "Data received"}), 200
        return jsonify({"status": "failure", "message": "No data"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def detect_road_conditions():
    global sensor_data
    while True:
        if sensor_data:
            latest_data = sensor_data[-1]
            accelerometer_data = next((item for item in latest_data if item.get('name') == 'accelerometer'), None)
            
            if accelerometer_data:
                acc_z = accelerometer_data['values'].get('z', 0)
                
                # Use Advanced Detection Engine
                condition = engine.process_reading(acc_z)
                current_loc = gps.get_location_string()

                print(f"[{current_loc}] Current Road State: {condition}")

                # Logging and CSV Export
                if config['data_handling']['logging_enabled']:
                    dataprocessing.log_detection(condition, current_loc, config['data_handling']['log_file'])
                
                if config['data_handling']['csv_export_enabled']:
                    dataprocessing.export_to_csv({
                        "condition": condition,
                        "z_variance": round(float(engine.z_buffer[-1]), 4) if engine.z_buffer else 0,
                        "location": current_loc
                    }, config['data_handling']['csv_file'])

        time.sleep(1.0 / detection_cfg['sampling_rate_hz'])

def run_flask_app():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()
    detect_road_conditions()
