import cv2

cap = cv2.VideoCapture(1) #this will use the 1st camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#on MAC, should use cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("myTestVideo.mp4",cv2.VideoWriter_fourcc(*'XVID'),fps=20,frameSize=(width,height))
'''Filename (如 "myTestVideo.mp4")：要写入的视频文件的名称和扩展名。
FourCC: 是用于指定视频编码方式的4-byte代码,如 'XVID'。
这是一种用于压缩数字视频的标准。可以通过 cv2.VideoWriter_fourcc() 来生成你想使用的编码方式。
在这里,'XVID' 是一种常见的编码方式,是 MPEG-4 编码标准的一种实现,用于创建 .mp4 或 .avi 文件。
Frames per second (FPS)：视频文件的帧率,表示每秒显示的图像帧数。注意在这里你的代码中并未明确指定 FPS 值。
Frame size: 视频帧的大小,以像素为单位,格式为（宽度,高度）。这个参数也未在你的代码中明确指定'''

while True:
    ret, frame = cap.read()

    #drawing
    writer.write(frame)

    #change it to gray scale
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #to display what camera read directly, not in gray scale
    cv2.imshow('Frame', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')): #wait for 1ms and when q is pressed, break
        break

cap.release()   #stop capturing video
writer.release()
cv2.destroyAllWindows() #close all windows
