import cv2
import numpy as np
import RPi.GPIO as GPIO
from yolov5.utils.torch_utils import select_device
from yolov5.models.common import DetectMultiBackend

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Green LED for fresh
GPIO.setup(23, GPIO.OUT)  # Red LED for rotten

# Load model
device = select_device('')
model = DetectMultiBackend('model/best.engine', device=device)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

  
    img = cv2.resize(frame, (640, 640))
    img = img[:, :, ::-1].transpose(2, 0, 1)  
    img = np.ascontiguousarray(img)

   
    results = model(img)

    # Parse results
    for *box, conf, cls in results.xyxy[0]:
        label = f"{int(cls)} {conf:.2f}"
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        if int(cls) == 0:  # Fresh
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
        else:  # Rotten
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)

    # results
    cv2.imshow("Fruit Quality Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
