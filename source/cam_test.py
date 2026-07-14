from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\runs\detect\train11\weights\best.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 🔥 IMPORTANT CHANGE (LOW CONF)
    results = model(frame, conf=0.10)

    annotated_frame = results[0].plot()

    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()