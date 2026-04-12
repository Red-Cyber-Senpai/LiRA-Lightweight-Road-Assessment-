"""
LiRA (Light-weight Road Assessment) - Web Interface
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Date: April 10, 2026
Description: Flask-based API for receiving and monitoring road condition sensor data.
Copyright (c) 2026 Saketcharan Chauhan M & Abubakr Siddiq Mohammed. All rights reserved.
"""

import requests
import matplotlib.pyplot as plt
import numpy as np
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

            # Analyze accelerometer data for road conditions
            accelerometer_data = next((item for item in latest_data if item.get('name') == 'accelerometer'), None)
            
            if accelerometer_data:
                acc_x = accelerometer_data['values'].get('x', 0)
                acc_y = accelerometer_data['values'].get('y', 0)
                acc_z = accelerometer_data['values'].get('z', 0)

                # Define threshold for detecting road conditions (adjust these based on your testing)
                pothole_threshold = 2.5  # A larger vertical spike likely indicates a pothole
                smooth_road_threshold = 0.5  # A low z-axis value indicates smooth road

                # Condition detection based on z-axis (vertical acceleration)
                if abs(acc_z) > pothole_threshold:
                    print(f"Alert: Pothole detected with z-acceleration: {acc_z}")
                elif abs(acc_z) < smooth_road_threshold:
                    print("Road condition: Smooth")
                else:
                    print("Road condition: Normal")

            else:
                print("No accelerometer data found in the latest reading.")

        time.sleep(2)  # Delay to prevent overwhelming the output

# Start Flask app in a separate thread
def run_flask_app():
    app.run(host='0.0.0.0', port=5000, debug=False)  # Run on port 5000

# Start the Flask app and the road condition detection
if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()  # Start Flask app in a new thread
    detect_road_conditions()  # Start detecting road conditions
