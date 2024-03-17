import cv2


ip = '192.168.1.100'  # put ip address here
port = '4747'
video_capture = cv2.VideoCapture(f"http://{ip}:{port}/video")


while True:
    ret, frame = video_capture.read()
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
