#!/bin/bash
#sudo avconv -y -r 1 -f video4linux2 -input_format mjpeg -i /dev/video0 -codec copy -r 24 /media/pi/BAOO/output.mpeg
#sudo avconv -y -f video4linux2 -video_size hd1080 -i /dev/video1 -r 24 ~/Desktop/output.avi
#ffmpeg -f v4l2 -framerate 30 -video_size 1920x1080 -c:v libx264 -i /dev/video0 -c:v copy output.avi
#ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv

## stream copy first
#ffmpeg -f v4l2 -framerate 18 -video_size 1920x1080 -input_format mjpeg -i /dev/video1 -c copy -an ~/Desktop/output.mkv
## re encode later
#ffmpeg -i mjpeg.mkv -c:v libx264 -crf 23 -preset medium -pix_fmt yuv420p out.mkv
ffmpeg -i ~/Desktop/output.mkv -s 1920x1080 -c:v libx264 -preset slower -crf 17 -c:a copy -y ~/Deskotp/out.mkv -async 1 -vsync 1

#ffmpeg -f v4l2 -framerate 90 -video_size 1920x1080 -input_format mjpeg -i /dev/video1 output.mkv
