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

        self.labelPic = QLabel(self)
        self.pixmap = QPixmap('logo.png')
        self.labelPic.setPixmap(self.pixmap)
        self.labelPic.move(50, 50)


        self.label = QLabel("Welcome to the Geologic Digitizer \n \n"
                            "1. Select an image of a graphic log to edit \n"
                            "2. Use the toolbar at the top of the page to select brush size, brush color, or eraser \n"
                            "3. Once done editing, select 'Reprune' \n"
                            "4. After final edits and repruning is complete, select 'Output CSV' "
                            "\n    to export your graphic log to a CSV file \n \n"
                            "While in the editor, you can select a new image to edit by clicking 'Select'. \n"
                            "Click on 'Next' to begin.\n",self)

        self.label.setFixedWidth(1200)

        self.label.setWordWrap(True)

        self.label.move(50, 250) # Move the Text to a location in the widget

        self.ToolsBTN = QPushButton('Next', self) # Create button object
        self.ToolsBTN.move(50, 600)

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
        
        global brushSize
        brushSize = 3

        global brushColor
        brushColor = Qt.black
        
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

    def scale(self, cv_obj):
        if cv_obj.shape[0] > 550: 
            scale = cv_obj.shape[0]/550
            cv_obj = cv2.resize(cv_obj, (int(cv_obj.shape[1]/scale), 550))
        return cv_obj
        
    # Function to convert qimage back into opencv object
    def create_cvobj(self, qimage):
        
        # Format RGB888!!!@!@!@
        qimage = qimage.convertToFormat(QImage.Format.Format_RGB888)

        width = qimage.width()
        height = qimage.height()
        print(width, height)

        # The 3 is the bytevalue within shape
        ptr = qimage.constBits()
        ptr.setsize(height * width * 3)
        
        arr = np.array(ptr).reshape(height, width, 3)
        return arr

    def reprune(self):
        qimage1 = self.qimage2.copy()
        
        cv_obj = self.create_cvobj(self.qimage2)
        cv_obj = self.scale(cv_obj)

        test = self.initiate_prune(cv_obj)
        test = self.scale(test)

        qimage2, h, w = self.create_qimage(test)

        cv2.imwrite("aprune.jpg", cv_obj)
        cv2.imwrite("bprune.jpg", test)

        self.qimage1 = qimage1
        self.qimage2 = qimage2

        self.label1.setPixmap(QPixmap.fromImage(self.qimage1))
        self.label2.setPixmap(QPixmap.fromImage(self.qimage2))
        self.label2.setImage(self.qimage2)
         
                 
    # Function to convert opencv objects into qimages
    # Returns qimage
    def create_qimage(self, cv_obj):
        height, width, byteValue = cv_obj.shape
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
        cvimage = self.scale(cvimage)
        self.qimage1, h, w = self.create_qimage(cvimage)
        self.label1.setPixmap(QPixmap.fromImage(self.qimage1))
          
        # Prune opencv object -> convert prune to qimage -> display it
        prune_image = self.initiate_prune(cvimage)
        prune_image = self.scale(prune_image)
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
        self.lastPoint = QPoint()

        mainMenu = self.parent.menuBar()
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColorMenu = mainMenu.addMenu("Brush Color")
        eraseMenu = mainMenu.addMenu("Erase")

        threepxAction = QAction("3px", self)
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction("5px", self)
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction("7px", self)
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction("9px", self)
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        blackAction = QAction("Black", self)
        brushColorMenu.addAction(blackAction)
        blackAction.triggered.connect(self.black)

        eraseAction = QAction("Erase", self)
        eraseMenu.addAction(eraseAction)
        eraseAction.triggered.connect(self.white)

        greenAction = QAction("Green", self)
        brushColorMenu.addAction(greenAction)
        greenAction.triggered.connect(self.green)

        yellowAction = QAction("Yellow", self)
        brushColorMenu.addAction(yellowAction) 
        yellowAction.triggered.connect(self.yellow)

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpeg *.jpeg);;ALL Files(*.*)")
        print(filePath)
        if filePath == "":
            return
        self.mQImage2.save(filePath)

    def threePx(self):
        global brushSize
        brushSize = 3

    def fivePx(self):
        global brushSize
        brushSize = 5

    def sevenPx(self):
        global brushSize
        brushSize = 7

    def ninePx(self):
        global brushSize
        brushSize = 9 

    def black(self):
        global brushColor
        brushColor = Qt.black

    def white(self):
        global brushColor
        brushColor = Qt.white
        global brushSize
        brushSize = 2

    def green(self):
        global brushColor
        brushColor = Qt.green

    def yellow(self):
        global brushColor
        brushColor = Qt.yellow
 
"""
This is a override class for QLabel. This implements canvas drawing functionality for QLabel objects which isnt possible without overriding. 
"""
class Label(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Label,self).__init__(parent=parent)

        self.image = QImage(0, 0, QImage.Format_RGB888)
        self.drawing = False
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
            painter.setPen(QPen(brushColor, brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False  

def Csv(QWidget): 
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent) 


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

        self.Window2.output_csv.clicked.connect(self.startCsv)

        self.show()

    def startCsv(self):

        # Setup Widget for Csv page
        self.Window3 = Csv(self)
        self.setWindowTitle("Output")
        self.setCentralWidget(self.Window3)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
