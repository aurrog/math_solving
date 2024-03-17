import cv2


ip = ''  # put your ip address here
port = '4747'
video_capture = cv2.VideoCapture(f"http://{ip}:{port}/video")


while True:
    ret, image = video_capture.read()

    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    # image = cv2.resize(image, (28, 28))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
