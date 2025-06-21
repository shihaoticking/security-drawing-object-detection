# Security Drawing Object Detection

A computer vision prototype for detecting doors in security drawings using YOLOv11n object detection model.

## Project Overview

This project implements a door detection system for security drawings using computer vision techniques. The system can:
- Identify doors in security drawing images
- Plot bounding boxes around detected doors
- Output results in structured JSON format with object locations and confidence scores

## Architecture

The project consists of two main components:

1. **Training Module** (`apps/training/`): Trains a YOLOv11n model on door detection dataset
2. **Inference App** (`apps/gradio_app/`): Gradio web interface for real-time door detection

## Installation

### Prerequisites
- Python 3.9+
- CUDA-compatible GPU (optional, for faster training)

### Setup

1. **Install base dependencies**:
   ```bash
   pip install -r requirements/base.txt
   ```

2. **Install Gradio app dependencies** (for inference):
   ```bash
   pip install -r requirements/gradio_app.txt
   ```

## Usage

### Training the Model

1. **Prepare your dataset** in YOLO format:
   ```
   dataset/
   ├── train/
   │   ├── images/
   │   └── labels/
   └── valid/
       ├── images/
       └── labels/
   ```

2. **Run training**:
   ```bash
   PYTHONPATH=. python apps/training/src/train.py
   ```

3. **Model will be saved** to `runs/train/exp/` and exported as ONNX format

### Running the Inference App

1. **Copy the trained model** (if you just finished training):
   ```bash
   cp runs/train/exp/weights/best.onnx models/
   ```

2. **Start the Gradio app**:
   ```bash
   PYTHONPATH=. python apps/gradio_app/src/gradio_app.py
   ```

3. **Access the web interface** at `http://localhost:7860`

4. **Upload an image** and click "Detect Doors" to see results

## Output Format

The system outputs detection results in JSON format:

```json
[
  {
    "x1": 926,
    "y1": 552,
    "x2": 1080,
    "y2": 720,
    "class": "door",
    "confidence": 0.9039
  }
]
```
