########################################################################
# Atuhor : Arun Jayan
# Email ID : <arunjayan32@gmail.com>
# This is Phase 1 Algorithm of Project TICA (version 1)
# completed on 30 july 2015 (phase 1 algo)
# using counting blue colored pixels 
########################################################################
### trying to do with centroid metheod but , i think for that method 
### it require more accuracy of images and  centroid  of our real world object should match with 
### our pre-setted region's centroid . So in a confusion .
########################################################################
"""
It can detect occurance of blue color in Region of Interest (ROI)
and also another code is created , track a blue color object using a mark on centroid after finding .
"""
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def count_ones(img,w,h):
	i,c = 0,0
	while(i<w):
		j=0
		while(j<h):
			if thresh[j,i]==255:
				c=c+1
			j=j+1
		i = i+1
	return c
def check_occurance(ones):
	if ones>200:
		duplicate[200:270, 240:310] = (25,156,255)
	else:
		duplicate[200:270, 240:310] = (255,15,20)
while True:
	_,frame = cap.read()
	#cv2.rectangle(frame,(200,225),(240,265),(255,0,0),0)
	duplicate = frame.copy()
	duplicate[200:270, 240:310] = (255,15,20)
	crop_img = frame[200:270, 240:310]
	hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2YCR_CB)
	thresh = cv2.inRange(hsv,np.array((150,75,145)),np.array((228,122,190)))
	#contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	#w = thresh.shape[1]
	#h = thresh.shape[0]
	ones = count_ones(thresh,thresh.shape[1],thresh.shape[0])
	check_occurance(ones)
	#print ones
	cv2.imshow("LiveFrame",duplicate)
	cv2.imshow("Threshold",thresh)
	cv2.imshow("ROI",crop_img)
	if cv2.waitKey(33)== 27:
		break
		#150,75,145

