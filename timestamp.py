import cv2
import datetime
import numpy as np
import time

stream = cv2.VideoCapture(1)
stream.set(3,1920)
stream.set(4,1080)
#fps_cam = cv2.CAP_PROP_FPS
#stream.set(5,30.0)
# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
video_writer = cv2.VideoWriter('Desktop/output.avi', fourcc, 24, (1920, 1080))

font = cv2.FONT_HERSHEY_COMPLEX

frame_count = 0
start_time = time.time()
time_interval = 3
frame_rate = 0
while True:
        end_time = time.time()
        success, frame = stream.read()
        if not success:
            break        
        if (end_time - start_time) > time_interval:
            frame_rate = int(frame_count / (end_time - start_time))
            start_time = time.time()
            frame_count = 0
        frame = cv2.flip(frame, 1)
        now = datetime.datetime.now()
        cv2.putText(frame, str(now),(0, 50), font, 1,(0,255,0), 2, cv2.LINE_AA)
        cv2.putText(frame, 'Fps :' + str(frame_rate),(0, 100), font, 1,(0,255,0), 2, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        video_writer.write(frame)
        frame_count += 1
        key = cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            break

# cleanup the stream and close any open windows
stream.release()
video_writer.release()
cv2.destroyAllWindows()
