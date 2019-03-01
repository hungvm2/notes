import cv2
import numpy as np
import argparse

#ap = argparse.ArgumentParser()
#ap.add_argument('-v', '--video', type=str, help='video file name')
#args = vars(ap.parse_args())


def face_cascade(frame):
    face_cascade = cv2.CascadeClassifier('/home/pi/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    face_count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        print(face_count, (x, y, x+w, y+h))
        face_count += 1

#filename = args.get('video')

stream = cv2.VideoCapture(0)

while True:
    success, frame = stream.read()
    if not success:
        break
    #face_cascade(frame)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
