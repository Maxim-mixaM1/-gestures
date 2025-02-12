from ultralytics import YOLO
import numpy as np
import cv2
model = YOLO('C:/PycharmProjects/pythonProject1/runs/detect/yolo_hand19/weights/best.pt')
img = cv2.imread('test_yolo.jpg')
results = model(img)[0]
img = results.orig_img
classes_names = results.names
classes = results.boxes.cls.cpu().numpy()
boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)
print(boxes)
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (192, 192, 192), (128, 128, 128), (128, 0, 0), (128, 128, 0),
    (0, 128, 0), (128, 0, 128), (0, 128, 128), (0, 0, 128), (72, 61, 139),
    (47, 79, 79), (47, 79, 47), (0, 206, 209), (148, 0, 211), (255, 20, 147)
]
grouped_objects = {}
for class_id, box in zip(classes, boxes):
        class_name = classes_names[int(class_id)]
        color = colors[int(class_id) % len(colors)]
        if class_name not in grouped_objects:
            grouped_objects[class_name] = []
        grouped_objects[class_name].append(box)
        x1, y1, x2, y2 = box
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
print(boxes[0][0])