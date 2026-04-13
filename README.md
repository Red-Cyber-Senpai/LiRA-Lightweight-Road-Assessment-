# LiRA (Light-weight Road Assessment)

![Project Status](https://img.shields.io/badge/Status-Development-orange)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-Proprietary-red)

## 👤 Developers
- **Saketcharan Chauhan M** (Co-Founder & Lead Developer)
- **Abubakr Siddiq Mohammed** (Co-Founder & Lead Researcher)

---

## 📝 Problem Statement
Deteriorating road conditions, including potholes and rough surfaces, pose constant safety hazards and cause significant vehicle damage. Identifying these defects at scale for infrastructure maintenance is typically manual, cost-prohibitive, and inefficient for modern smart cities.

## 🚀 Approach
The **LiRA (Light-weight Road Assessment)** Project delivers an intelligent, automated road condition monitoring system. It fuses **Sensor-based Machine Learning** for fast tactile anomaly detection with **Image-based Artificial Intelligence** (YOLOv8) for secondary visual confirmation, creating a reliable and cost-effective mapping solution for road maintenance.

## 🚀 Key Features
- **Advanced Dual-Validation:** Combines Vertical Variance Analysis (Sliding Window Standard Deviation) for precision and YOLOv8 for visual confirmation.
- **Centralized Management:** Full system control via `config.yaml`.
- **GPS Integration:** Integrated location handling for mapping road defects.
- **Automated Reporting:** Real-time log file generation and CSV data export for analytical assessment.
- **Modular Architecture:** Clean separation of detection, processing, and hardware interfacing.

## 🛠 Technology Stack
- **Language:** Python 3.9+
- **Configuration:** PyYAML
- **Algorithms:** NumPy-based Variance Analysis
- **Machine Learning:** Scikit-learn, Joblib
- **Computer Vision:** OpenCV, Ultralytics YOLOv8
- **Framework:** Flask (Web Interface)
- **Data Handling:** CSV, Logging

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

## 📊 Results
LiRA's dual-validation architecture significantly reduces false positives by leveraging standard deviation variance across sensor inputs before validating via the YOLOv8 visual classifier. The centralized architecture successfully maps road defects accurately to integrated GPS coordinates in real-time.

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
