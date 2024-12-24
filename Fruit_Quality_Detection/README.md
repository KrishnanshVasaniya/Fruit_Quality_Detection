# Fruit Quality Detection System

This project implements a real-time fruit quality detection system using NVIDIA Jetson Nano and YOLOv5. 
It identifies fruits as fresh or rotten, making it ideal for automated sorting applications.

## Features
- Real-time fruit quality detection using YOLOv5.
- Edge deployment on Jetson Nano for low latency.
- Visual bounding boxes and category labels (Fresh/Rotten).
- GPIO-controlled LED indicators for classification feedback.

## Hardware Requirements
- NVIDIA Jetson Nano
- USB Camera
- LED Indicators (Red and Green)
- Power Supply for Jetson Nano
- Monitor, Keyboard, and Mouse (for initial setup)

## Software Requirements
- Python 3.8+
- NVIDIA JetPack SDK (includes CUDA, TensorRT)
- YOLOv5 Framework

## Installation Steps

### 1. Setup the Hardware
1. Connect the USB Camera to the Jetson Nano.
2. Attach LEDs to GPIO pins (e.g., pin 18 for green, pin 23 for red).
3. Ensure a stable power supply for Jetson Nano.

### 2. Install JetPack SDK
- Download and install the JetPack SDK from the [NVIDIA Developer Site](https://developer.nvidia.com/embedded/jetpack).
- This includes essential tools like CUDA and TensorRT.

### 3. Clone the YOLOv5 Repository
Run the following commands to download YOLOv5 and install dependencies:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### 4. Install Additional Dependencies
Run the following commands to install required Python libraries:
```bash
pip install opencv-python torch numpy RPi.GPIO
```

### 5. Prepare the YOLOv5 Model
- Train a YOLOv5 model on a custom dataset (fresh and rotten fruits) or download a pre-trained model.
- Convert the model to TensorRT format for optimized inference:
```bash
python export.py --weights best.pt --include engine
```

### 6. Run the Inference Script
Run the following command to start the fruit quality detection system:
```bash
python3 inference.py
```

## Usage
1. Start the system by running the inference script.
2. Observe the real-time video feed with detected fruits categorized as "Fresh" or "Rotten."
3. Green LED will light up for fresh fruits, and Red LED will light up for rotten fruits.

## Acknowledgements
Special thanks to the YOLOv5 and NVIDIA developer communities for their tools and documentation.

## License
This project is licensed under the MIT License.
