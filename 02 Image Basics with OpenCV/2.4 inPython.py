import cv2
import numpy as np  

##############
## FUNCTION ##
############## 

#event is what mouse does, like a right click or left click. x, y is the coordinate
def draw_circle(event,x,y,flags,param):
    #mouse event is left mouse buttom click down
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),radius=100,color=(0,255,0),thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),radius=100,color=(255,0,0),thickness=-1)


#connect this function with the img
cv2.namedWindow(winname="My_Drawing")
#setMouseCallback会返回鼠标情况，包括event，x,y坐标
cv2.setMouseCallback('My_Drawing',draw_circle)

#############################
## SHOWING IMG WITH OPENCV ##
#############################

img = np.zeros(shape=(512,512,3),dtype=np.int8)
while True:
    cv2.imshow("My_Drawing", img)
    if(cv2.waitKey(20) & 0xFF == 27):
        break
cv2.destroyAllWindows()