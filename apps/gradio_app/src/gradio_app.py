from typing import Tuple

import gradio as gr
from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Boxes

model = YOLO('models/best.onnx', task='detect', verbose=True)

def box_to_json(box: Boxes) -> dict:
    """
    Convert a box to a JSON object.
    """
    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().tolist()
    return {
        "x1": int(x1),
        "y1": int(y1),
        "x2": int(x2),
        "y2": int(y2),
        "class": model.names[int(box.cls[0].cpu().numpy())],
        "confidence": float(box.conf[0].cpu().numpy())
    }

def inference(image: Image) -> Tuple[Image, dict]:
    """
    Inference the image using the YOLO model.
    """
    results = model.predict(image)

    return results[0].plot(), [box_to_json(box) for box in results[0].boxes]


with gr.Blocks(title="YOLOv11n Object Detection", theme=gr.themes.Default()) as demo:
    with gr.Row():
        # Left column
        with gr.Column(scale=1):
            gr.Markdown("### Upload Image")
            input_image = gr.Image(
                label="Upload Image",
                type="pil"
            )
            detect_btn = gr.Button(
                "Detect Doors",
                variant="primary"
            )
        
        # Right column
        with gr.Column(scale=1):
            gr.Markdown("### Detection Results")
            output_image = gr.Image(
                label="Detected Objects"
            )
            
            gr.Markdown("### Detection Data (JSON)")
            json_output = gr.JSON(
                label="Bounding Boxes and Classifications",
                height=200
            )
    
    # Connect the button to the processing function
    detect_btn.click(
        fn=inference,
        inputs=[input_image],
        outputs=[output_image, json_output]
    )


demo.launch()
