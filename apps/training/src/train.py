import torch
import yaml
from ultralytics import YOLO


def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def detect_device():
    """Automatically detect and return the best available device"""
    if torch.cuda.is_available():
        device = '0'  # Use first GPU
        print(f"GPU detected: {torch.cuda.get_device_name(0)}")
        print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
    else:
        device = 'cpu'
        print("No GPU detected, using CPU")
    return device


config = load_config('configs/training.yaml')

# Auto-detect device and update config
if config['device'] == 'auto':
    config['device'] = detect_device()

# Adjust batch size based on device
if config['device'] == 'cpu':
    config['batch_size'] = min(config['batch_size'], 8)  # Smaller batch for CPU
    print(f"Using CPU, adjusted batch size to {config['batch_size']}")
else:
    # For GPU, we can use larger batch size
    config['batch_size'] = min(config['batch_size'], 32)  # Cap at 32 for GPU
    print(f"Using GPU, batch size: {config['batch_size']}")

model = YOLO("yolo11n.pt")  # YOLOv11 nano model

# Train the model
results = model.train(
    data="configs/dataset.yaml",
    epochs=config['epochs'],
    imgsz=config['img_size'],
    batch=config['batch_size'],
    patience=config['patience'],
    device=config['device'],
    workers=config['workers'],
    project=config['project'],
    name=config['name'],
    exist_ok=config['exist_ok'],
    pretrained=config['pretrained'],
    optimizer=config['optimizer'],
    verbose=config['verbose']
)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Export the model to ONNX format
success = model.export(format="onnx", dynamic=True)
print(f"Model exported to ONNX: {success}")
