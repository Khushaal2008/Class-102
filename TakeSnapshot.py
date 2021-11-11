import cv2

def take_snapshot():

    videoCapture = cv2.VideoCapture(0)

    result = True
    while(result):
        ret, frame = videoCapture.read()

        cv2.imwrite("NewPhoto.png", frame)

        result = False

    videoCapture.release()
    cv2.destroyAllWindows()

take_snapshot()