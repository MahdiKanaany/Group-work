import cv2
camera = cv2.VideoCapture(0)

while (True):
     ret,  capture = camera.read()
     color = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)
     cv2.imshow("webcam",color)
     if cv2.waitKey(1) == ord("q"):break
camera.release()
cv2.destroyAllwindows()

