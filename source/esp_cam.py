from ultralytics import YOLO
import cv2
import requests
import numpy as np
import time

model = YOLO(r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\runs\detect\train11\weights\best.pt")

url = "http://192.168.4.1/capture"

while True:
    try:
        res = requests.get(url, timeout=5)
        img_arr = np.array(bytearray(res.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

        if frame is None:
            continue

        results = model(frame, conf=0.05)

        print(results[0].boxes)  # debug

        annotated = results[0].plot()
        cv2.imshow("Detection", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        time.sleep(1)

    except:
        print("Reconnect...")
        time.sleep(2)

cv2.destroyAllWindows()