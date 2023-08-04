import cv2
import time

def draw_circle(event,x,y,flags,param):
    global center, click
    if(event == cv2.EVENT_LBUTTONDOWN):
        if(click == True):
            center = (0,0)
            click = False
        if(click == False):
            center = (x,y)
            click = True
    
click = False
center = (0,0)

cap = cv2.VideoCapture(1)
cv2.namedWindow("test")
cv2.setMouseCallback("test",draw_circle)

while True:
    ret, frame = cap.read()

    if(click == True):
        cv2.circle(frame,center=center,radius=5,color=(255,0,0),thickness=-1)
    cv2.imshow("test", frame)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()