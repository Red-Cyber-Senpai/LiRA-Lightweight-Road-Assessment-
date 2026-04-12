"""
LiRA (Light-weight Road Assessment) - YOLOv8 Model Training
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
Date: April 10, 2026
Description: Script to train the YOLOv8 model for pothole detection using Roboflow datasets.
Copyright (c) 2026 Saketcharan Chauhan M & Abubakr Siddiq Mohammed. All rights reserved.
"""

from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8-seg.pt")  # Using YOLOv8 segmentation model

# Define the dataset URL from Roboflow (replace with your actual URL)
roboflow_dataset_url = "YOUR_ROBOFLOW_DATASET_URL"

# Train the model
model.train(data=roboflow_dataset_url, epochs=50, imgsz=640)

# Save the model
model.save("pothole_detection_model.pt")
