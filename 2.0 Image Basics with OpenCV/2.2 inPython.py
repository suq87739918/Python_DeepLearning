import cv2  
img = cv2.imread('/Users/sunyueqian/Desktop/Python Computer Vison/DATA/00-puppy.jpg')
#print(img)
while True:
    cv2.imshow('puppy', img)
    #if we wait for at laest 1ms AND we press the ESC 
    if cv2.waitKey(1) & 0xFF == 27:
        #break
        break
cv2.destroyAllWindows
