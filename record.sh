#!/bin/bash
#sudo avconv -y -r 1 -f video4linux2 -input_format mjpeg -i /dev/video0 -codec copy -r 24 /media/pi/BAOO/output.mpeg
sudo avconv -y -f video4linux2 -video_size hd720 -i /dev/video0 -qscale 1 /media/pi/BAOO/output.avi
#python3 /home/pi/Desktop/face_cascade.py --video /media/pi/BAOO/output.avi
#-input_format mjpeg -c:v copy
#ffmpeg -f v4l2 -framerate 30 -video_size 1920x1080 -c:v libx264 -i /dev/video0 -c:v copy output.avi
