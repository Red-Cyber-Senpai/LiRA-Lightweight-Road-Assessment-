"""
LiRA (Light-weight Road Assessment) - Data Processing Module
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Description: Functions for filtering noise, preparing images, and logging results.
"""

import numpy as np
import datetime
import csv
import os

def log_detection(condition, location="Unknown", log_file="logs/lira_system.log"):
    """
    Logs a detection event with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {condition} at {location}\n"
    
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(f"Logged: {log_entry.strip()}")

def export_to_csv(data_dict, csv_file="data/road_assessment_log.csv"):
    """
    Exports a dictionary of data to a CSV file for analytical assessment.
    """
    file_exists = os.path.isfile(csv_file)
    fields = ["timestamp", "condition", "z_variance", "location"]
    
    # Adding timestamp if not present
    if "timestamp" not in data_dict:
        data_dict["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_dict)

def filter_vibration_noise(data, threshold=0.1):
    """
    Remove low-level noise from sensor readings to prevent false positives.
    """
    filtered = [v if abs(v) > threshold else 0 for v in data]
    return filtered

def normalize_acceleration(data):
    """
    Normalize acceleration values to a standard range for the machine learning model.
    """
    if len(data) == 0:
        return data
    max_val = max(abs(np.array(data)))
    if max_val == 0:
        return data
    return [v / max_val for v in data]

def prepare_yolo_frame(frame):
    """
    Resize and normalize camera frames before sending them to the YOLOv8 model.
    """
    # Placeholder for computer vision preprocessing
    # In a real scenario, this would involve cv2.resize and color correction
    return frame

if __name__ == "__main__":
    test_data = [0.05, 1.2, -2.1, 0.02, 3.4]
    print(f"Original: {test_data}")
    print(f"Filtered: {filter_vibration_noise(test_data)}")
    print(f"Normalized: {normalize_acceleration(test_data)}")
