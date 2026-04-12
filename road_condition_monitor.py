"""
LiRA (Light-weight Road Assessment) - Road Condition Monitor
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Date: April 10, 2026
Description: Real-time sensor data analysis and pothole detection logic.
Copyright (c) 2026 Saketcharan Chauhan M & Abubakr Siddiq Mohammed. All rights reserved.
"""

import requests
import threading
import time
from flask import Flask, request, jsonify

# Flask app to receive HTTP POST requests
app = Flask(__name__)

# Data storage for received sensor data
sensor_data = []

# Function to receive sensor data via HTTP POST
@app.route('/data', methods=['POST'])
def receive_sensor_data():
    global sensor_data
    try:
        data = request.json  # Assuming the data is sent in JSON format
        if data:  # Ensure data is not empty
            sensor_data.append(data)  # Store the received data
            return jsonify({"status": "success", "message": "Data received"}), 200
        else:
            return jsonify({"status": "failure", "message": "No data received"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Function to detect road conditions based on sensor data
def detect_road_conditions():
    global sensor_data
    while True:
        if sensor_data:
            latest_data = sensor_data[-1]  # Get the latest sensor data
            sensor_name = latest_data.get('name', 'Unknown')

            # Example: Analyze sensor data for road conditions
            acceleration = latest_data.get('values', {}).get('z', 0)  # Using 'z' as a simple road condition indicator

            # Logic for detecting road conditions based on acceleration data
            if sensor_name == 'accelerometer':
                if acceleration > 10:  # Example threshold for a pothole or bump
                    print("Alert: Pothole or bump detected!")
                elif acceleration < 3:  # Example threshold for a smooth road
                    print("Road condition: Smooth")
                else:
                    print("Road condition: Normal")

        time.sleep(2)  # Delay to prevent overwhelming the output

# Start Flask app in a separate thread
def run_flask_app():
    app.run(host='0.0.0.0', port=5000, debug=False)  # Run on port 5000

# Start the Flask app and the road condition detection
if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()  # Start Flask app in a new thread
    detect_road_conditions()  # Start detecting road conditions
