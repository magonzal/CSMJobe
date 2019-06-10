#!/usr/bin/env python

#######################################################################################
# Name:         ImageReader
#
# Last Updated: 5/18/19
#
#######################################################################################
import cv2
import imutils
import numpy as np
import tkinter as tk

class ImageReader:

    def __init__(self, image): 
        """
        
        """
        self.image = image
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() 
        if(screen_height >= 650):
            scale = self.image.shape[0]/650
            self.image = cv2.resize(self.image, (int(self.image.shape[1]/scale), 650))

    def set_image(self, img):
        """
    
        """

        self.image = img

    def get_image(self, img):
        """
        
        """
        return self.image
    
    def prune(self):
        """


        """
        thresh = cv2.Canny(self.image, 10, 55)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        canvas = np.add(np.zeros(self.image.shape, np.uint8),255)
        points = {}
        layer = 1
        
        for c in contours:
            if cv2.contourArea(c) >  200:
                points_array = []
                approx = cv2.approxPolyDP(c, 0.00001*cv2.arcLength(c, True), True)
                cv2.drawContours(canvas, [approx], -1, (0, 0, 0), 2)
                for point in c:
                    points_array.append( (point[0][0], point[0][1] ) )
                points[layer] = points_array
                layer+=1
        return canvas, points



def main():
    test = cv2.imread('test3.jpg') 
    canv, _ = ImageReader(test).prune()
    cv2.imshow('test', canv)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

