<h1 align="center">🚗 Driven-Car: Driver Drowsiness Detection System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg" alt="OpenCV">
  <img src="https://img.shields.io/badge/dlib-Facial%20Landmarks-orange.svg" alt="dlib">
  <img src="https://img.shields.io/badge/Tkinter-GUI-lightgrey.svg" alt="Tkinter">
</p>

<p align="center">
  <b>A real-time Driver Drowsiness Detection application built to ensure road safety by monitoring the driver's eye aspect ratio (EAR) using computer vision.</b>
</p>

---

## 📖 Overview

Driver fatigue is a significant factor in a large number of vehicle accidents. This project aims to prevent such accidents by continuously monitoring the driver's eyes using a webcam. If the system detects that the driver's eyes have been closed for a specified duration, it will trigger an alarm to wake the driver up.

The system utilizes **dlib's** pre-trained facial landmark detector to locate eyes and calculates the **Eye Aspect Ratio (EAR)** to determine if the eyes are open or closed.

## ✨ Key Features

- 🎥 **Real-Time Monitoring**: Captures live video feed from the webcam.
- 👁️ **Eye Tracking & EAR**: Calculates the Eye Aspect Ratio in real-time.
- ⏱️ **Duration Thresholding**: Triggers an alert only if the eyes remain closed beyond a safe duration (default 2 seconds).
- 🔊 **Audio Alarm**: Plays a loud alert sound when drowsiness is detected.
- 🖥️ **Interactive GUI**: Easy-to-use interface built with Tkinter, featuring controls to start/stop the camera and test the alarm.

## 🛠️ Technology Stack

- **Python**: Core programming language.
- **OpenCV**: Video capture and image processing.
- **dlib**: Face detection and 68 facial landmark prediction.
- **SciPy**: Euclidean distance calculations for EAR.
- **Tkinter & PIL**: Graphical User Interface.
- **Pygame**: Audio alarm playback.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8 or newer installed on your system. You will also need a functional webcam.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M0-Adly/Driven-Car-.git
   cd Driven-Car-
   ```

2. **Download the pre-trained model:**
   - Ensure the dlib model `shape_predictor_68_face_landmarks.dat` is correctly placed in the project structure (or download it if it's missing).

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the main application script:

```bash
python Drowsiness_GUI.py
```

- Click **Start Camera** to begin monitoring.
- The system will track your eyes and display the *Eyes Closed Time*.
- If you close your eyes for more than 2 seconds, an alert will be triggered.
- Click **Stop Camera** to end the session.

---
<p align="center">
</p>
