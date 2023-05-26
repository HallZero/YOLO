from ultralytics import YOLO
import cv2 as cv

img = cv.imread(r"cracks\assets\9ea1d4d6-cc21-48dc-b214-a09e26f436961627385689.webp")
model = YOLO("./best.pt")

result = model.predict(img, conf=0.6)
cv.imshow("results", result[0].plot())
cv.imwrite("results.jpg", result[0].plot())

cv.waitKey(0)
cv.destroyAllWindows()