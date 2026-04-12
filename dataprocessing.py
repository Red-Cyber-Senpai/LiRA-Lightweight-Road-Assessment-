"""
LiRA (Light-weight Road Assessment) - Data Processing Module
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Description: Functions for filtering noise from accelerometer data and preparing images for YOLO.
"""

import numpy as np

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
