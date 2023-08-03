import cv2

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#top left corner
x = width // 2  # "//" will retuin in integer, not in float, ex: 10 // 5 => 2, not 2.0
y = height // 2

#width and height of rectangle
w = width // 4
h = height // 4

#bottom right corner = (x + w, y + h)

while True:
    ret,frame = cap.read()

    cv2.rectangle(frame,pt1=(x,y),pt2=(w+x,h+y),color=(0,0,255),thickness=4)
    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
cap.release()
cv2.destroyAllWindows()