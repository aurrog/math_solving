import cv2
import time
import numpy as np


ip = '192.168.1.100'  # put your ip address here
port = '4747'
video_capture = cv2.VideoCapture(f"http://{ip}:{port}/video")

is_photo = False

while True:
    ret, image = video_capture.read()

    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.imwrite(image_path, cleaned)
    # cv2.imshow('image', cleaned)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        symbol = image[y:y + h, x:x + w]

    cv2.imshow('', contours)

    # cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('w'):
        is_photo = True
        break


video_capture.release()
cv2.destroyAllWindows()

if is_photo:
    cv2.imshow('photo', image)
    time.sleep(2)
    cv2.waitKey(0)
