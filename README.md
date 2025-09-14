# Simple Face Recognition Attendance System

This project implements a **real-time face recognition system** using Python, OpenCV, and the `face_recognition` library. It can be used as an **attendance system** to automatically identify people from reference images, saving time compared to manual attendance marking.

## Features
- Detect faces in real-time using a webcam
- Recognize known faces from reference images
- Label detected faces with names
- Automate attendance tracking
- Simple and easy-to-use Python implementation

## Project Structure
- `main.py` – runs the webcam, detects faces, and displays them with names
- `simple_facerec.py` – contains the `SimpleFacerec` class for encoding and detecting faces
- `Pictures/` – folder to store images of people to recognize (filename = label)

## Libraries Used
- `face_recognition` – for face detection and encoding
- `opencv-python` – for accessing webcam and drawing on frames
- `numpy` – for numerical operations and handling face coordinates

## Setup
1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/simple-facerec.git
cd simple-facerec
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install opencv-python face_recognition numpy
```

> Note: `face_recognition` may require `dlib` and `cmake`.

## Usage
1. Add reference images to `Pictures/` (filename = name)  
2. Run:

```bash
python main.py
```

3. The webcam window will open showing detected faces with names. Press `ESC` to exit.

## Purpose
Automated attendance system that saves time by recognizing faces and marking attendance automatically.
