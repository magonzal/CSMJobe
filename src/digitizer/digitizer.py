#/usr/bin/env python

#######################################################################################
# Name:         Digitizer 
#
# Last Updated: 5/18/19
#
#######################################################################################

import sys
import tkinter
import cv2
from csv_creation import CSVCreation
from plotter import plotCreator
from image_reader import ImageReader
from digitizerGUI import Gui


def main(argv): 
    gui = Gui(tkinter.Tk(), "Geological Digizer V 1.0")
    cv_image = cv2.imread('victory.png')
    print('here')
    image_reader = ImageReader(cv_image)
    canvas, layers = image_reader.prune()
    cv2.imshow('test', canvas)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    print('hereeeeeeeeeeeeeeeeeeeeeeeeee')
    csv = CSVCreation(layers).output_csv()
    plotCreator(csv).getLayers()


if __name__ == '__main__':
    main(sys.argv)
