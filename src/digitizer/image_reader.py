#!/usr/bin/env python

#######################################################################################
# Name:         ImageReader
#
# Last Updated: 5/18/19
#
#######################################################################################
import cv2
import imutils


class ImageReader:

    def __init__(self, image): 
		self.image = image
		scale = self.image.shape[0]/650
		self.image = cv2.resize(self.image, (int(self.image.shape[1]/scale), 650))

	
	@image.setter
	def image(self, img):
		self.image = img

	def get_image(self, img):
		return self.image
	
	def prune(self):
		thresh = cv2.Canny(img, 10, 55)
		contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		
		for c in contours:
        	if cv2.contourArea(c) >  200:
            	approx = cv2.approxPolyDP(c, 0.0001*cv2.arcLength(c, True), True)
                cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)

		return self.image





