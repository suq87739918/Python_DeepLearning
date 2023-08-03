import cv2
import time

#这个视频会播放的很快，因为目的是给电脑看的，不是给人看的
cap = cv2.VideoCapture('/Users/sunyueqian/Desktop/Python Computer Vison/myTestVideo.mp4')

if(cap.isOpened() == False):
    print("ERROR FILE NOT FOUND or WRONG CODEC USED")
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:

        #the video is recorded in 20FPS, so set it delay 1/20 for each frame to display
        time.sleep(1/20)

        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()