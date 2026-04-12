# LiRA (Light-weight Road Assessment) Technical Documentation

**Version:** 1.0.0  
**Date:** April 10, 2026  
**Lead Developers:** Saketcharan Chauhan M and Abubakr Siddiq Mohammed

---

## 1. Introduction
The **LiRA (Light-weight Road Assessment)** Project is an intelligent road condition monitoring system designed to detect potholes, rough roads, and smooth road surfaces using a combination of sensor-based machine learning and image-based artificial intelligence.

## 2. System Architecture
The LiRA system consists of five major layers:
1.  **Data Collection Layer:** Captures raw accelerometer data (X, Y, Z axes) and image frames.
2.  **Data Processing Layer:** Noise filtering, normalization, and feature extraction.
3.  **Machine Learning Layer:** Uses a **Random Forest** model to classify road conditions based on vibration patterns.
4.  **Computer Vision Layer:** Uses the **YOLOv8** object detection model to visually identify potholes.
5.  **Output and Reporting Layer:** Combines signals from both sensors and cameras for a reliable final decision.

## 3. Machine Learning Methodology
### 3.1 Random Forest (Sensor Data)
- **Dataset:** UCI Human Activity Recognition Dataset (utilized for vibration pattern simulation).
- **Process:** The model analyzes the Z-axis (vertical) acceleration spikes to distinguish between normal driving and pothole impacts.
- **Accuracy:** Evaluated using Precision, Recall, and F1 Score.

### 3.2 YOLOv8 (Image Detection)
- **Dataset:** Roboflow Pothole Dataset.
- **Algorithm:** You Only Look Once (YOLO) v8 for real-time inference.
- **Output:** Bounding boxes with confidence scores.

## 4. Hardware and Deployment
The system is designed to be lightweight and efficient, allowing deployment on:
-   **Smartphones:** Utilizing built-in accelerometers and cameras.
-   **Edge Devices:** Like Raspberry Pi or NVIDIA Jetson Nano.
-   **Autonomous Systems:** Integrated into the vehicle navigation stack.

## 5. Future Scalability
-   **Cloud Integration:** Real-time analytics dashboard for city authorities.
-   **GPS Mapping:** Automatically marking road defects on a global map.
-   **Predictive AI:** Scheduling road repairs based on the rate of degradation.

---

## 📜 Intellectual Property
This technical documentation and the associated implementation are the joint property of **Saketcharan Chauhan M** and **Abubakr Siddiq Mohammed**. No part of this work may be reproduced without explicit permission.
