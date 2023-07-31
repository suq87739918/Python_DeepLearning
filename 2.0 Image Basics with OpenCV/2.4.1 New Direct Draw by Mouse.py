import cv2
import numpy as np  

###############
## VARIABLES ##
###############

#drawing will become True if the mouse is pressed down, False if the mouse button is up
drawing = False
ix = -1
iy = -1

##############
## FUNCTION ##
############## 

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    #原理是：如果鼠标一直移动，那么就会一直画图，所以当把鼠标拉回来或者反向移动时，图像会很怪
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),color=(0,255,0),thickness=-1)
    #当鼠标左键抬起来时，根据当前坐标画图
    elif event ==cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),color=(0,255,0),thickness=-1)

#############################
## SHOWING IMG WITH OPENCV ##
#############################


###########
## BLANK ##
###########

img = np.zeros((512,512,3),dtype=np.int8)
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:
    cv2.imshow("my_drawing",img) #windows name: my_drawing
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()