# LiRA (Light-weight Road Assessment)

![Project Status](https://img.shields.io/badge/Status-Development-orange)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-Proprietary-red)

## 👤 Developers
- **Saketcharan Chauhan M** (Co-Founder & Lead Developer)
- **Abubakr Siddiq Mohammed** (Co-Founder & Lead Researcher)

---

## 📝 Project Overview
The **LiRA (Light-weight Road Assessment)** Project is an intelligent road condition monitoring system designed to detect potholes, rough roads, and smooth road surfaces. By leveraging a combination of **Sensor-based Machine Learning** and **Image-based Artificial Intelligence**, LiRA provides a highly reliable and cost-effective solution for infrastructure maintenance and smart city transportation.

## 🚀 Key Features
- **Dual-Validation Detection:** Combines Accelerometer data and Computer Vision (YOLOv8) for high-accuracy results.
- **Real-Time Processing:** Designed for deployment on low-cost hardware and edge devices.
- **Predictive Maintenance:** Helps city authorities identify road damage before it becomes severe.
- **Modular Architecture:** Easy to scale and integrate with autonomous vehicle systems.

## 🛠 Technology Stack
- **Language:** Python 3.x
- **Machine Learning:** Scikit-learn, NumPy, Pandas, Joblib
- **Computer Vision:** OpenCV, Ultralytics YOLOv8
- **Framework:** Flask (Web Interface)
- **Hardware Support:** Smartphones, Edge Devices, Embedded Systems

## 📂 Project Structure
```text
LiRA Project/
├── app.py                      # Flask-based API interface
├── road_condition_monitor.py   # Core sensor analysis logic
├── train_model.py              # YOLOv8 training script
├── config.yaml                 # System configurations
├── checklibraries.py          # Dependency validation script
├── dataprocessing.py           # Data cleaning & normalization
├── README.md                   # Project overview
├── DOCUMENTATION.md            # Detailed technical docs
├── data/                       # Sensor datasets (UCI HAR)
└── dataset/                    # Image datasets (Roboflow)
```

## 🔨 Setup and Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Red-Cyber-Senpai/LiRA-Lightweight-Road-Assessment-.git
   cd LiRA-Project
   ```
2. **Setup Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Verify Installation:**
   ```bash
   python checklibraries.py
   ```

---

## 📜 Copyright
Copyright © 2026 **Saketcharan Chauhan M** and **Abubakr Siddiq Mohammed**. All rights reserved.
This project is proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
