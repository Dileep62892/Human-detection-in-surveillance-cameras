# Human Detection in Surveillance Cameras

## Overview
The **Human Detection in Surveillance Cameras** is a real-time project that detects humans in video streams using the Histogram of Oriented Gradients (HOG) algorithm. When a human is detected, the system captures an image and sends an email alert. This project is useful for enhancing security in public spaces, monitoring pedestrian traffic, and preventing accidents.

## Features
1. **Real-Time Detection**: The system continuously analyzes video frames from a camera feed and identifies pedestrians in real time.
2. **Email Alert**: Upon detecting a human, the system captures an image and sends an email notification to a specified recipient.
3. **Customizable Parameters**: You can adjust detection parameters (e.g., window stride, padding, scale) to fine-tune the system's performance.
4. **Minimal False Positives**: The HOG-based approach minimizes false positives, making it suitable for practical applications.

## Algorithms
### Histogram of Oriented Gradients (HOG)
- The HOG algorithm computes gradient histograms in local image regions.
- It represents the shape and texture of objects by analyzing the distribution of gradient orientations.
- HOG is particularly effective for detecting pedestrians due to its robustness against variations in lighting and pose.

## Getting Started
1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/Dileep62892/Human-detection-in-surveillance-cameras.git

3. **Install Dependencies**:
   - Python 3.x
   - OpenCV
   - smtplib (for email notifications)

   ```bash
    pip install opencv-python imutils

4. **Configure Email Settings**:
   - Open human.py.
   - Set your Gmail address and password.
   - Update the recipient’s email address (toadd).

## Usage
1. Run the human detection script:
   
    ```bash
    python human.py

3. Press ‘q’ to exit the application.
