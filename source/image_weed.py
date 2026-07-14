import cv2
import requests
import numpy as np
from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

# ESP32-CAM stream URL
url = "http://192.168.1.45/capture"   # change to your ESP32 IP

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Crop vs Weed Detection", annotated)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()