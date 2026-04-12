"""
LiRA (Light-weight Road Assessment) - Dependency Checker
Developed by: Saketcharan Chauhan M & Abubakr Siddiq Mohammed
"""

import sys

def check_libraries():
    required = {
        "flask": "Flask (Web API)",
        "requests": "Requests (HTTP Client)",
        "matplotlib": "Matplotlib (Visualization)",
        "numpy": "NumPy (Math/Logic)",
        "ultralytics": "Ultralytics (YOLOv8)",
        "cv2": "OpenCV (Computer Vision)",
        "pandas": "Pandas (Data Handling)",
        "sklearn": "Scikit-Learn (Machine Learning)",
        "joblib": "Joblib (Model Loading)"
    }
    
    missing = []
    print("Checking LiRA Project Dependencies...")
    print("-" * 30)

    for module, name in required.items():
        try:
            __import__(module)
            print(f"[OK] {name}")
        except ImportError:
            missing.append(name)
            print(f"[MISSING] {name}")

    print("-" * 30)
    if not missing:
        print("All dependencies are satisfied. Ready for deployment!")
    else:
        print(f"Warning: {len(missing)} libraries are missing.")
        print("Please run: pip install -r requirements.txt")

if __name__ == "__main__":
    check_libraries()
