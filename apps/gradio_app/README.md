# Door Detection Gradio App

A Gradio interface for door detection using YOLOv11n model.

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements/base.txt  # shared packages
   pip install -r requirements/gradio_app.txt
   ```

2. **Verify Model**:
   Ensure the trained YOLOv11n model is available at `models/best.onnx`

## Usage

Direct Python Execution
```bash
PYTHONPATH=. python3 apps/gradio_app/src/gradio_app.py
```

## Access the App

Once running, open your web browser and navigate to:
```
http://localhost:7860
```

## How to Use

1. **Upload Image**: Use the file uploader on the left to select an image
2. **Run Detection**: Click the "Detect Doors" button
3. **View Results**: 
   - See the annotated image with bounding boxes in the top right
   - Check the JSON output below for detailed detection data

## JSON Output Format

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
