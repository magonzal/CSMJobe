#!/usr/bin/env python

#######################################################################################
# Name:         ImageReader
#
# Last Updated: 5/18/19
#
#######################################################################################
import cv2
import numpy as np
import tkinter as tk
from point import Point
from layer import Layer
from csv_creation import CSVCreation


class ImageReader:

    def __init__(self, image): 
        """
        Initializes ImageReader object and then scales it by factor.
        :param image: OpenCV object
        """
        self.image = image
        #root = tk.Tk()
        #screen_height = root.winfo_screenheight()
        #if self.image.shape[0] >= 650:
        #    scale = self.image.shape[0]/650
        #    self.image = cv2.resize(self.image, (int(self.image.shape[1]/scale), 650))

    def set_image(self, img):
        """
        Sets the image to another OpenCV object
        :param img: OpenCV object
        :return: Nothing
        """

        self.image = img

    def get_image(self):
        """
        Returns the OpenCV object
        :return:
        """
        return self.image
    
    def prune(self):
        """
        This function calculates a threshold using the canny algorithm, then using that threshold it finds the necessary
        contours of the OpenCV image. Then it iterates through the contours and finds all the contours that have an area
        larger than 200, which gave the best results. This also populates a dictionary with all the points corresponding
        to each layer. The contours are drawn on a white canvas
        :return: Canvas with drawn contours and dictionary points
        """

        thresh = cv2.Canny(self.image, 1, 300)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        canvas = np.add(np.zeros(self.image.shape, np.uint8), 255)
        layers = []
        layer_id = 1
        
        for c in contours:
            if cv2.contourArea(c) > 150:
                layer = Layer(layer_id)
                points_array = []

                approx = cv2.approxPolyDP(c, 0.0001*cv2.arcLength(c, True), True)
                cv2.drawContours(canvas, [approx], -1, (0, 0, 0), 5)
                for point in c:
                    points_array.append(Point(point[0][0], point[0][1]))
                
                layer.layer_name="test"
                layer.points = points_array
                layers.append(layer)
                # append layer to layers aray
                layer_id += 1
        return canvas, layers

    def filter(self, kernel=(5, 5)):
        """
        Simple filter that can be used to filter the image.
        :param kernel: Kernel size to convolve the image with
        :return: Filtered OpenCV image
        """
        kernel = np.ones(kernel, np.float32) / 25
        return cv2.filter2D(self.image, -1, kernel)

    def gaussian_blur(self, kernel=(5, 5)):
        """
        Blurs the image by using a gaussian kernel
        :param kernel: Kernel tuple
        :return: Gaussian Blurred image
        """
        return cv2.GaussianBlur(self.image, kernel, 0)

    def average_blur(self, kernel=(5, 5)):
        """
        Blurs the image by simply averaging pixels within the image
        :param kernel: The size of the kernel to average the image
        :return: Averaged Blurred Image
        """
        return cv2.blur(self.image, kernel)

    def median_blur(self, noise=5):
        """
        Takes the median of the image based on noise level
        :param noise: Noise level
        :return: Median Blurred Image
        """
        return cv2.medianBlur(self.image, noise)




def main():
    test = cv2.imread('victory.png')
    canv, _ = ImageReader(test).prune()
    woop = CSVCreation(_)
    woop.output_csv()
    cv2.imshow('test', canv)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

