from ultralytics import YOLO
import cv2
import requests
import numpy as np
import time

model = YOLO(r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\runs\detect\train11\weights\best.pt")

url = "http://192.168.4.1/capture"

while True:
    try:
        response = requests.get(url, timeout=5)
        img_array = np.array(bytearray(response.content), dtype=np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is None:
            print("❌ No frame")
            time.sleep(1)
            continue

        results = model(frame, conf=0.05)
        annotated = results[0].plot()

        cv2.imshow("ESP Detection", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        time.sleep(1)

    except Exception as e:
        print("⚠️ reconnecting...", e)
        time.sleep(2)

cv2.destroyAllWindows()