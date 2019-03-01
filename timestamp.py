import cv2
import datetime
import numpy as np

stream = cv2.VideoCapture(1)
stream.set(3,1280)
stream.set(4,1024)
#fps_cam = cv2.CAP_PROP_FPS
#stream.set(5,30.0)
# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
video_writer = cv2.VideoWriter('Desktop/output.avi', fourcc, 11, (1280, 720))

font = cv2.FONT_HERSHEY_COMPLEX


while True:
        success, frame = stream.read()
        if not success:
            break        
        frame = cv2.flip(frame, 1)
        now = datetime.datetime.now()
        cv2.putText(frame, str(now),(0, 50), font, 1,(0,255,0), 2, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        video_writer.write(frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            break

# cleanup the stream and close any open windows
stream.release()
video_writer.release()
cv2.destroyAllWindows()
