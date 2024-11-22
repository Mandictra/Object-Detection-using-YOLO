from ultralytics import YOLO
import cv2


model = YOLO('../yolo-weights/yolov8n.pt')
results = model("hello/3.jpeg", show = True)
cv2.waitKey(0)