import cv2

#callback function rectangle
def draw_rectangle(event,x,y,flags,param):
    #update golbal variables
    global pt1,pt2,topLeft_clicked,bottomRight_clicked
    if(event == cv2.EVENT_LBUTTONDOWN):
        #Reset the rectangle(check the rectangle is already there)
        if(topLeft_clicked == True & bottomRight_clicked == True):
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
        if(topLeft_clicked == False):
            pt1 = (x,y)
            topLeft_clicked = True
        elif(bottomRight_clicked == False):
            pt2 = (x,y)
            bottomRight_clicked = True

#global variables
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

#connect to the callback function
cap = cv2.VideoCapture(1)
cv2.namedWindow("test")
cv2.setMouseCallback("test",draw_rectangle)

while True:
    ret,frame = cap.read()

    #drawing on the frame based on the global variables
    if(topLeft_clicked == True):
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    if(topLeft_clicked == True & bottomRight_clicked == True):
        cv2.rectangle(frame,pt1,pt2,color=(0,0,255),thickness=3)

    cv2.imshow("test", frame)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
cap.release()
cv2.destroyAllWindows()