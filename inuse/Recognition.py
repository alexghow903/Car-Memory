import cv2
import time
import parselp
import tojson
from ultralytics import YOLO


CONFIDENCE_THRESHOLD = 0.65
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
frame_rate = 4
prev = 0
while True:
	time_elapsed = time.time() - prev
	ret, frame = cap.read()
	if time_elapsed > 1./frame_rate:
		if not ret:
			break
		
		# run the YOLO model on the frame
		detections = model(frame)[0]

		results = []

		for data in detections.boxes.data.tolist():
			# extract the confidence (i.e., probability) associated with the prediction
			confidence = data[4]

			# filter out weak detections by ensuring the 
			# confidence is greater than the minimum confidence
			if float(confidence) < CONFIDENCE_THRESHOLD:
				continue

			# if the confidence is greater than the minimum confidence,
			# get the bounding box and the class id
			xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
			class_id = int(data[5])
			# add the bounding box (x, y, w, h), confidence and class id to the results list
			if class_id == 2:
				results.append([[xmin, ymin, xmax - xmin, ymax - ymin], confidence, class_id])
		for i in results:
			cropped_frame = frame[i[0][1]:(i[0][1]+i[0][3]), i[0][0]:(i[0][0]+i[0][2])]
			# cv2.imshow('madam', cropped_frame)
			# cv2.waitKey(0)
			text = parselp.contour(cropped_frame)
			if text != "null":
				tojson.check(text)
	
	prev = time.time()

    