import sys
import cv2
import numpy as np
import copy

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from image_reader import ImageReader

"""
PANE 1: Welcome Page
    - Contains information about the program and how to use it
    - Talk about the different features of the program
    - Authors because credit for our work is nice
"""
class Welcome(QWidget):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)

        self.label = QLabel("Welcome", self) # Create object that contains text
        self.label.move(50, 50) # Move the Text to a location in the widget

        self.ToolsBTN = QPushButton('Next', self) # Create button object
        self.ToolsBTN.move(50, 350) 

"""
PANE 2: Upload/Edit/Save Page
    - THREE Buttons:
        1) Select and upload an Image
        2) Reprune (takes the second image and sets it as the first image then prunes the first image again)
        3) Save (Create CSV)
"""
class UploadImage(QWidget):
    def __init__(self, parent=None):
        super(UploadImage, self).__init__(parent)
        
        self.parent = parent
        self.parent.resize(100, 100)
        self.height = 0
        self.width = 0
        
        # Used to create menubar after the user uploads an image the first time
        self.first_upload = True

        # Initialize two labels that will store the two images
        self.label1 = QLabel(self)
        self.label2 = Label(self)
        
        # Create the three buttons to upload/edit/save
        self.select_img = QPushButton('Select', self)
        self.prune = QPushButton('Reprune', self)
        self.output_csv = QPushButton('Output CSV', self)

        # Move the buttons so theyre aesthetic af
        self.select_img.move(10, 10 + self.height)
        self.prune.move(10, 40 + self.height)
        self.output_csv.move(10,70 + self.height)

        # Make the buttons listen to me
        self.select_img.clicked.connect(self.upload_image)
        self.prune.clicked.connect(self.reprune)

        # Array of layers (will be used to create CSV when user is done)
        self.layers = None
    
    def create_cvobj(self, qimage):

        qimage = qimage.convertToFormat(QImage.Format.Format_RGB32)

        width = qimage.width()
        height = qimage.height()

        ptr = qimage.bits()
        ptr.setsize(height * width * 4)
        
        arr = np.array(ptr).reshape(height, width, 4)
        return arr

    def reprune(self):
        qimage1 = self.qimage2.copy()
        
        cv_obj = self.create_cvobj(qimage1)
        
        tempo = (cv_obj.shape[0], cv_obj.shape[1], 3)

        test = self.initiate_prune(cv_obj)

        cv2.imwrite("PRUNED_NOW_FIRST.jpg", cv_obj)
        cv2.imwrite("PRUNE_ON_PRUNE.jpg", test)

        qimage2, h, w = self.create_qimage(test)

        self.label1.setPixmap(QPixmap.fromImage(qimage1))
    

        pix = QPixmap.fromImage(qimage2)
        pix.scaledToWidth(w)
        pix.scaledToHeight(h)

        self.label2.setPixmap(pix)
        self.label2.setImage(qimage2)
         

        self.qimage1 = qimage1
        self.qimage2 = qimage2
        
        print("heit wif: " + str(h) + ", " + str(w))

        print("image 1: " + str(self.qimage1.height()))
        print("image 1: " + str(self.qimage1.width()))
  
        print("image 2 fff: " + str(qimage2.height()))
        print("image 2 fff: " + str(qimage2.width()))
         
        print("image 2: " + str(self.qimage2.height())) 
        print("image 2: " + str(self.qimage2.width()))
  
    # Function to convert opencv objects into qimages
    # Returns qimage
    def create_qimage(self, cv_obj):
        height, width, byteValue = cv_obj.shape
        print(byteValue)
        byteValue = byteValue * width

        cv2.cvtColor(cv_obj, cv2.COLOR_BGR2RGB, cv_obj)
        return QImage(cv_obj, width, height, byteValue, QImage.Format_RGB888), height, width

    # Function to prune opencv object, and save the layers. 
    # Returns pruned image as opencv object
    def initiate_prune(self, cv_obj):
        pruned, layers = ImageReader(cv_obj).prune()
        self.layers = layers
        return pruned
    
    # Functionality for the select image button
    # Will handle opening an image and displaying it along with the pruned image
    def upload_image(self):
        # Open File Prompt
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File')
        
        # Get opencv object -> convert to qimage -> display it
        cvimage = cv2.imread(fname)
        self.qimage1, h, w = self.create_qimage(cvimage)
        self.label1.setPixmap(QPixmap.fromImage(self.qimage1))
          
        # Prune opencv object -> convert prune to qimage -> display it
        prune_image = self.initiate_prune(cvimage)
        self.qimage2, h2, w2 = self.create_qimage(prune_image)
        self.label2.setPixmap(QPixmap.fromImage(self.qimage2))
        self.label2.move(w+10, 0)
        
        # Resize labels to fit full height/width of images
        self.label1.resize(w, h)
        self.label2.resize(w2, h2)

        # Move buttons below images
        self.select_img.move(10, h+10)
        self.prune.move(10, h+40)
        self.output_csv.move(10, h+70)

        # Resize entire widget to fit the images and buttons
        self.parent.resize(w * 2 + 10, h + 120)
        self.show()
        
        # Set image in label for the drawing functionality
        self.label2.setImage(self.qimage2)
        
        if self.first_upload:
            self.first_upload = False
            self.create_menubar() 

    # Function to populate the menu bar
    def create_menubar(self):
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.parent.menuBar()
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")

        saveAction = QAction("Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.save)

        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Ctrl+C")

        threepxAction = QAction("3px", self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction("5px", self)
        fivepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction("7px", self)
        sevenpxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction("9px", self)
        ninepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        blackAction = QAction("Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)

        whiteAction = QAction("White", self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)

        greenAction = QAction("Green", self)
        greenAction.setShortcut("Ctrl+W")
        brushColor.addAction(greenAction)

        yellowAction = QAction("Yellow", self)
        yellowAction.setShortcut("Ctrl+R")
        brushColor.addAction(yellowAction) 

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpeg *.jpeg);;ALL Files(*.*)")
        print(filePath)
        if filePath == "":
            return
        self.mQImage2.save(filePath)

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9 

 

class Label(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Label,self).__init__(parent=parent)

        self.image = QImage(0, 0, QImage.Format_RGB32)
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

    def paintEvent(self, e):
        super().paintEvent(e)
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.image.rect(), self.image)
        
    def setImage(self, image):
        self.image = image
        self.qimage2 = image

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton & self.drawing:
            painter = QPainter(self.qimage2)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False  



########################################################################################
#
# Main Window that controls all the widget view or panes
#   - Pane 1: Welcome Page
#   - Pane 2: Upload/Edit/Prune
#   - Pane 3: ???
#
########################################################################################

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.startWelcome()

    def startWelcome(self):

        # Setup Widget for Welcome page
        self.Window = Welcome(self)
        self.setWindowTitle("Digitizer")
        self.setCentralWidget(self.Window)

        # Button Listener to initiate next Widget
        self.Window.ToolsBTN.clicked.connect(self.startUploadImage)

        self.show()

    def startUploadImage(self):
        
        # Setup Widget for Upload page
        self.Window2 = UploadImage(self)
        self.setWindowTitle("Upload Log")
        self.setCentralWidget(self.Window2)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
