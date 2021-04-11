
import serial
comNumber = input("Please enter the com number (for COM2 type 2, for example)\n> ")
try:
	ser = serial.Serial("COM" + comNumber, baudrate = 2000000) #, timeout = 0
except:
	print("Error while opening Serial: COM" + str(comNumber))
	

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
#from pygame import mixer
import numpy as np
import imutils
import time
import cv2
import os
import math


#system libraries
import os
import sys
from threading import Timer
import shutil
import time

# import zmq

# ctx = zmq.Context()
# pub = ctx.socket(zmq.PUB)
# pub.setsockopt(zmq.SNDHWM, 2)
# pub.bind('tcp://*:5555')


sX = 1
oX = 0
sY = 1
oY = 0

def scale(val, src, dst):
    """
    basically el map() de arduino
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

detections = None 
OLDlocs = 0
OLDpreds = 0
checking = 0
global var
var = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
global var2
var2 = 2
	
def detect_and_predict_mask(frame, faceNet, maskNet,threshold):
	global OLDlocs
	global OLDpreds
	global checking
	# grab the dimensions of the frame and then construct a blob
	# from it
	global detections 
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()
	# initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	locs = []
	preds = []
	# loop over the detections

	for i in range(0, detections.shape[0]):
		# extract the confidence (i.e., probability) associated with
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is
		# greater than the minimum confidence
		if confidence >threshold:
			# compute the (x, y)-coordinates of the bounding box for
			# the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)
			
			# add the face and bounding boxes to their respective
			# lists
			locs.append((startX, startY, endX, endY))
			#print(maskNet.predict(face)[0].tolist())
			preds.append(maskNet.predict(face)[0].tolist())
			OLDlocs = locs
			OLDpreds = preds
	else: 
		locs = OLDlocs
		preds = OLDpreds
	return (locs, preds)




# SETTINGS
MASK_MODEL_PATH=os.getcwd()+"\\model\\mask_model.h5"
FACE_MODEL_PATH=os.getcwd()+"\\face_detector" 
SOUND_PATH=os.getcwd()+"\\sounds\\alarm.wav" 
THRESHOLD = 0.5

# Load Sounds
#mixer.init()
#sound = mixer.Sound(SOUND_PATH)

# load our serialized face detector model from disk
#print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([FACE_MODEL_PATH, "deploy.prototxt"])
weightsPath = os.path.sep.join([FACE_MODEL_PATH,"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
#print("[INFO] loading face mask detector model...")
maskNet = load_model(MASK_MODEL_PATH)

# initialize the video stream and allow the camera sensor to warm up
#print("[INFO] starting video stream...")
vs = VideoStream(0).start()
#time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	#frame = imutils.resize(frame, width=400) #################make screen smaller######################
	original_frame = frame.copy()
	# detect faces in the frame and determine if they are wearing a
	# face mask or not

	try:
		(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet,THRESHOLD)
		for (box, pred) in zip(locs, preds):
			# unpack the bounding box and predictions
			(startX, startY, endX, endY) = box
			(mask, withoutMask) = pred

			# determine the class label and color we'll use to draw
			# the bounding box and text
			label = "Mask" if mask > withoutMask else "No Mask"
			#if(label=="No Mask") and (mixer.get_busy()==False):
			#    sound.play()
			color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
			if label == "Mask":
				var2 = 0 
			else:
				var2 = 1

			# include the probability in the label
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

			# display the label and bounding box rectangle on the output
			# frame
			cv2.putText(original_frame, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(original_frame, (startX, startY), (endX, endY), color, 2)
			cv2.rectangle(frame, (startX, startY+math.floor((endY-startY)/1.6)), (endX, endY), color, -1)
				
			#output the face coordenates and other info
			#startX, startY, endX, endY
			averageX = (startX + endX)/2
			averageY = (startY + endY)/2
			averageX = scale(averageX, (0.0, 640), ((-90*sX)+90, +(90*sX)+90))
			averageY = scale(averageY, (0.0, 640), ((-90*sY)+90, +(90*sY)+90))
			averageX = averageX + oX
			averageY = averageY + oY
			#a = str(averageX) + "_" + str(averageY) + "_" + str(round((mask*100), 2)) + "_" + str(round((withoutMask*100), 2))
			message = "{0:03d}".format(int(averageX)) + "{0:03d}".format(int(averageY))
			#pub.send_string(message)
			try:
				ser.write(bytes(message, 'utf-8'))
				#print(message)
			except Exception as e: print(e)
						
			
			#cv2.circle(original_frame, (int(averageX), int(averageY)), 3, (0, 255, 255), -1) #preview the face center, the target
			cv2.addWeighted(frame, 0.5, original_frame, 0.5 , 0,frame)
			
			#time.sleep(0.1)

	except:
		pass
		
	################### doing the mask average for shooting
	suma = 0
	var = str(var) + str(var2)
	var = var[1:101] #A + 1
	for char in var:
		suma += int(char)
	if suma == 100: #A
		print("s")
		#ser.write(("s"))
		#pub.send_string("s")   #.encode(encoding='UTF-8'))
		var = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
	#pub.send_string(str(suma) + "(suma) | " + str(var2) + " (var2) | " + str(var) + " (var)")
	###################
	# show the output frame
	#frame= cv2.resize(frame,(640,480))
	cv2.imshow("UwU CUM", frame)
	key = cv2.waitKey(1) & 0xFF
	
	# wasd
	if key == ord("w"):
		print("W")
		oY += -5

	if key == ord("a"):
		print("A")
		oX += 5

	if key == ord("s"):
		print("S")
		oY += 5

	if key == ord("d"):
		print("D")
		oX += -5


	#ijkl
	if key == ord("i"):
		print("I")
		sY += 0.05

	if key == ord("j"):
		print("J")
		sX += -0.05

	if key == ord("k"):
		print("K")
		sY += -0.05

	if key == ord("l"):
		print("L")
		sX += 0.05
	
	#print("X= " + str(averageX) + " Y= " + str(averageY) + "oX=" + str(oX) + " oY=" + str(oY) + " sX=" + str(sX) + " sY=" + str(sY))
	#q
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()