import cv2
import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import time


#splash image path
splash_image = "/home/sv-v1/projects/picasso/images/Musical Picasso 1.png"
#splash UI path
splash_ui = "/home/sv-v1/projects/picasso/gui/splashscreen/splash.ui"
#Image Folder Path
path_folder = "/home/sv-v1/projects/picasso/images/"
#Width of slideshow
slideshow_width = 1500
#Height of slideshow
slideshow_height = 1000
#Transition time slideshow
slideshow_trasnition_time = 2
#Image stable time
slideshow_img_time = 3
#Window Name
window_name="Musical Picasso"
#Supoorted formats tuple
supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.dib', '.jpe', '.jp2', '.pgm', '.tiff', '.tif', '.ppm')
#Escape ASCII Keycode
esc_keycode=27
#Enter ASCII Keycode
enter=13
#slide calibration
transit_slides = 10
#minimum weight
min_weight = 0
#maximum weight 
max_weight = 1


#Range function with float 
def range_step(start, step, stop):
	range = start
	while range < stop:
		yield range
		range += step

#Wait Key function with escape handling		
def wait_key(time_seconds):
	#state False if no Esc key is pressed
	state = False
	#Check if any key is pressed. second multiplier for millisecond: 1000
	k = cv2.waitKey(int(time_seconds * 1000))
	#Check if ESC key is pressed. ASCII Keycode of ESC=27
	if k == esc_keycode:  
		#Destroy Window
		cv2.destroyWindow(window_name)
		#state True if Esc key is pressed
		state = True
	if k == enter:
		cv2.destroyWindow(window_name)
		state = True
	
	#return state	
	return state	
	
#Load image path of all images		
def load_img_path(pathFolder):
	#empty list
	_path_image_list = []
	#Loop for every file in folder path
	for filename in os.listdir(pathFolder):
		#Image Read Path
		_path_image_read = os.path.join(pathFolder, filename)
		#Check if file path has supported image format and then only append to list
		if _path_image_read.lower().endswith(supported_formats):
			_path_image_list.append(_path_image_read)

	#Return image path list
	return _path_image_list
#Load image and return with resize	
def load_img(pathImageRead, resizeWidth, resizeHeight): 	
	#Load an image
	#cv2.IMREAD_COLOR = Default flag for imread. Loads color image.
	#cv2.IMREAD_GRAYSCALE = Loads image as grayscale.
	#cv2.IMREAD_UNCHANGED = Loads image which have alpha channels.
	#cv2.IMREAD_ANYCOLOR = Loads image in any possible format
	#cv2.IMREAD_ANYDEPTH = Loads image in 16-bit/32-bit otherwise converts it to 8-bit
	_img_input = cv2.imread(pathImageRead,cv2.IMREAD_ANYCOLOR)

	#Check if image is not empty
	if _img_input is not None:
		#Get read images height and width
		_img_height, _img_width = _img_input.shape[:2]
	
		#if image size is more than resize perform cv2.INTER_AREA interpolation otherwise cv2.INTER_LINEAR for zooming
		if _img_width > resizeWidth or _img_height > resizeHeight:
			interpolation = cv2.INTER_AREA
		else:
			interpolation = cv2.INTER_LINEAR
		
		# perform the actual resizing of the image and show it
		_img_resized = cv2.resize(_img_input, (resizeWidth, resizeHeight), interpolation)
	else:
		#if image is empty
		_img_resized = _img_input
	#return the resized image	
	return _img_resized	



"""
.......................................................................................................

Splash screen starts

.......................................................................................................
"""

class ThreadProgress(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        i = 0
        while i<101:
            time.sleep(0.1)
            self.mysignal.emit(i)
            i += 1

FROM_SPLASH,_ = uic.loadUiType(os.path.join(os.path.dirname(__file__),splash_ui))
        
class Splash(QtWidgets.QMainWindow, FROM_SPLASH):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        Qtwidgets.QMainWindow.setFullScreen()
        pixmap = QtGui.QPixmap(splash_image)
        self.splah_image.setPixmap(pixmap.scaled(350, 300))
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
        
    @QtCore.pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 100:
            self.close()
            slideshow()

"""
.......................................................................................................

Splash screen ends

.......................................................................................................
"""



"""
.......................................................................................................

Welcome screen starts

.......................................................................................................
"""

class Welcome(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')
        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


"""
.......................................................................................................

Welcome screen ends

.......................................................................................................
"""



"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Slideshow starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

def slideshow():
	#Load image paths	
	img_path_list = load_img_path(path_folder)
	#slideshow transition image wait time
	slideshow_transit_wait_time = float (slideshow_trasnition_time) / transit_slides
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
	#Create first image	
	img_one = None	
	#Laod every image file path
	for imge_path in img_path_list:
		#if image is none load image
		if img_one is None:
			#Load first image
			img_one = load_img(imge_path, slideshow_width, slideshow_height)
			#Show image in window
			cv2.imshow(window_name, img_one)
			# wait for slide show time to complete and break if Esc key pressed
			if wait_key(slideshow_img_time):
				break
			#continiue to for loop
			continue

		#Load Second image	
		img_two = load_img(imge_path, slideshow_width, slideshow_height)

		#for loop through every weight in range 
		for weight_two in range_step(min_weight, float (max_weight)/transit_slides, max_weight):
			#substract weight_two from max_weight to get weight_one 
			weight_one = max_weight - weight_two
			#Weighted addition opertion
			#img_one: First image
			#weight_one: Wight for imge one
			#img_two: Second image
			#weight_two: Wight for imge two
			#0: gamma
			slide_img = cv2.addWeighted(img_one, weight_one, img_two,weight_two, 0)
			#Show image in window
			cv2.imshow(window_name, slide_img)
			# wait for slide show time to complete and clear image path list and also break if Esc key pressed
			if wait_key(slideshow_transit_wait_time):
				del img_path_list[:]
				break


		# wait for slide show time to complete and break if Esc key pressed
		if wait_key(slideshow_img_time):
			break
		#copy image two to image one	
		img_one = img_two

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Slideshow ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""



"""

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())




class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')
        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()
"""


class Controller:

    def __init__(self):
        pass

    def show_splash(self):
        self.splash = Splash()
#        self.splash.switch_window.connect(self.show_main)
        self.splash.show()

    def Welcome(self):
        self.welcome = Welcome()
#        self.welcome.switch_window.connect(self.show_main)
        self.welcome.show()



app=QtWidgets.QApplication(sys.argv)
controller = Controller()
controller.show_splash()
controller.Welcome()
sys.exit(app.exec_())


