# USAGE
# python fps_demo.py
# python fps_demo.py --display 1

# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

def face_cascade(frame, url):
	face_count = 0
	face_cascade = cv2.CascadeClassifier(url)
	faces = face_cascade.detectMultiScale(frame, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
		print(face_count, (x, y, x+w, y+h))
		face_count += 1

# created a *threaded *video stream, allow the camera senor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()

# loop over some frames...this time using the threaded stream
#while fps._numFrames < args["num_frames"]:
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=720)

	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		face_cascade(frame,'/home/pi/NewXML/haarcascade_frontalface_default.xml')
		#face_cascade(frame,'/home/pi/NewXML/haarcascade_profileface.xml')
		cv2.imshow("Frame", frame)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] number of frames: {:.2f}".format(fps._numFrames))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()