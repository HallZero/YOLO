from ultralytics import YOLO
import cv2 as cv

video_capture = cv.VideoCapture(0)
model = YOLO("pokemon\poke.pt")

while True:
    _, frame = video_capture.read()
    result = model.predict(frame, conf=0.6)
    cv.imshow("results", result[0].plot())

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
