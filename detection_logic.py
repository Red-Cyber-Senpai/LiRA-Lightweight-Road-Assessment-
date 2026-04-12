"""
LiRA (Light-weight Road Assessment) - Detection Logic
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Description: Robust sliding-window analysis for road condition classification.
"""

import numpy as np

class RoadDetectionEngine:
    def __init__(self, pothole_threshold=2.5, smooth_threshold=0.5, window_size=10):
        self.pothole_threshold = pothole_threshold
        self.smooth_threshold = smooth_threshold
        self.window_size = window_size
        self.z_buffer = []

    def process_reading(self, z_accel):
        """
        Processes a single z-axis acceleration reading and returns the road condition.
        Uses sliding window variance to reduce false positives.
        """
        self.z_buffer.append(z_accel)
        if len(self.z_buffer) > self.window_size:
            self.z_buffer.pop(0)

        # Standard deviation provides a better measure of 'roughness' than a single point
        if len(self.z_buffer) < 2:
            return "Initialising"

        current_variance = np.std(self.z_buffer)
        
        # Logic for classification
        if current_variance > self.pothole_threshold:
            return "Pothole detected"
        elif current_variance < self.smooth_threshold:
            return "Smooth"
        else:
            return "Normal"

    def update_thresholds(self, pothole, smooth):
        self.pothole_threshold = pothole
        self.smooth_threshold = smooth
