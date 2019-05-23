import cv2
import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import time
import imutils
from imutils import paths
from pygame import mixer
import random

app = QtWidgets.QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()

#Music files path
music_path = "/home/sv-v1/projects/picasso/music/"
#splash image path
splash_image = "/home/sv-v1/projects/picasso/images/Musical Picasso.png"
#splash UI path
splash_ui = "/home/sv-v1/projects/picasso/gui/splashscreen/splash.ui"
#Image Folder Path
path_folder = "/home/sv-v1/projects/picasso/images/"
#Width of slideshow
slideshow_width = width
#Height of slideshow
slideshow_height = height
#Transition time slideshow
slideshow_trasnition_time = 2
#Image stable time
slideshow_img_time = 3
#Window Name
window_name="Musical Picasso"
#Supoorted formats tuple
supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.dib', '.jpe', '.jp2', '.pgm', '.tiff', '.tif', '.ppm')
#supproted music formats
supported_formats_msc = ('.wav', '.mp3')
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
#image styling models
models="/home/sv-v1/projects/picasso/neural-style-transfer/models"



"""
.......................................................................................................

Splash screen starts

.......................................................................................................
"""

class ThreadProgress(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):

        QtCore.QThread.__init__(self, parent=None)
    def run(self):
        i = 0
        while i<101:
            time.sleep(0.05)
            self.mysignal.emit(i)
            i += 1


class Ui_Splash(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(width, height)
        Splash.showFullScreen()
        print("----------------Screen Size--------------------\n\nWidth \theight")
        print(width,"\t", height)
        print("\n-----------------------------------------------\n")

        self.centralwidget = QtWidgets.QWidget(Splash)
        self.centralwidget.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(587, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(600, 448, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 3, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap((QtGui.QPixmap(splash_image)).scaled(550,550))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(600, 448, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 3, 3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(587, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 2, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("background-color: rgb(210, 219, 230);")
#        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(587, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 2)
        Splash.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Splash)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName("menubar")
        Splash.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Splash)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Splash.setStatusBar(self.statusbar)

    @QtCore.pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 100:
            Splash.hide()
            slideshow()

"""
.......................................................................................................

Splash screen ends

.......................................................................................................
"""





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
		cv2.destroyAllWindows()
		#state True if Esc key is pressed
		state = True
	if k == enter:
		cv2.destroyAllWindows()
		state = True
		controller.Welcome()
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
        
	_path_image_list = sorted(list(_path_image_list))
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




def load_msc_path(mscfolder):
	#empty list
	_path_msc_list = []
	#Loop for every file in folder path
	for filename in os.listdir(mscfolder):
		#music Read Path
		_path_msc_read = os.path.join(mscfolder, filename)
		print(_path_msc_read)
		#Check if file path has supported image format and then only append to list
		if _path_msc_read.lower().endswith(supported_formats_msc):
			_path_msc_list.append(_path_msc_read)
	print(_path_msc_list)
	random.shuffle(list(_path_msc_list))
#Return image path list
	return _path_msc_list

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Slideshow starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

def slideshow():
	#Load image paths	
	img_path_list = load_img_path(path_folder)
	#load music path list
	music_path_list = load_msc_path(music_path)
	#slideshow transition image wait time
	slideshow_transit_wait_time = float (slideshow_trasnition_time) / transit_slides
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
	#Create first image	
	img_one = None	
	i = 0
	print(music_path_list)
	#Laod every image file path
#	while True:
#	for msc_path in music_path_list:
	for imge_path in img_path_list:
		mixer.music.load(music_path_list[i])
		mixer.music.play()
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
		i+=1
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
.......................................................................................................

Welcome screen starts

.......................................................................................................
"""

class Welcome(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Musical-PiCasso')
        self.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.showFullScreen()
        layout = QtWidgets.QGridLayout()
#        QtCore.QTimer.setSingleShot(False)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Welcome\n\n To \n\nPiCasso Art Creator")
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.label)
        vbox.addStretch()
        self.setLayout(vbox)
#        QtCore.QTimer.setSingleShot(True)
        QtCore.QTimer.singleShot(3000, controller.show_menu)
#        QtCore.QTimer.singleShot(self,False)

"""
.......................................................................................................

Welcome screen ends

.......................................................................................................
"""


"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Picasso Page Starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


class Picasso(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Picasso, self).__init__(parent)
        self.setWindowTitle('Picasso Image Creator')
#        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.setGeometry(0,0,width, height)
#        self.show()
        modelPaths = paths.list_files(models, validExts=(".t7",))
        modelPaths = sorted(list(modelPaths))
        cap = cv2.VideoCapture(0)
        cv2.namedWindow("Capture", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Capture",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        while (1):
            ret, frame = cap.read()
            cv2.imshow("Capture", frame)
            k = cv2.waitKey(1)
            if k == ord("s"):
                mixer.music.load(music_path+"shutter_sound.wav")
                mixer.music.play()
                cv2.imwrite("/home/sv-v1/projects/picasso/extracted_images/style_capture.jpg", frame)
                cv2.destroyAllWindows()
                cap.release()
                break

# loop over the model paths
        for modelPath in modelPaths:
# load the neural style transfer model from disk
            print("[INFO] loading {}...".format(modelPath))
            net = cv2.dnn.readNetFromTorch(modelPath)
# load the input image, resize it to have a width of 600 pixels,
# then grab the image dimensions
            image = frame
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]

# construct a blob from the image, set the input, and then
# perform a forward pass of the network
            blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),(103.939, 116.779, 123.680), swapRB=False, crop=False)
            net.setInput(blob)
            output = net.forward()
# reshape the output tensor, add back in the mean subtraction,
# and then swap the channel ordering
            output = output.reshape((3, output.shape[2], output.shape[3]))
            output[0] += 103.939
            output[1] += 116.779
            output[2] += 123.680
            output /= 255.0
            output = output.transpose(1, 2, 0)

# show the images
#            cv2.imshow("Input", image)
            cv2.namedWindow("Output", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Output",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("Output", output)
            key = cv2.waitKey(0)
            if key == ord("s"):
                cv2.imwrite("/home/sv-v1/projects/picasso/images/save.png", output)
#                im = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
#                cv2.imwrite("/home/sv-v1/projects/picasso/images/2.jpeg", im)
                cv2.destroyAllWindows()
                del modelPaths[:]
                self.close()
                slideshow()
                break

"""
        row = col = 0
        imagesPerRow = 3
        pics = []
        pathFolder = "/home/sv-v1/projects/picasso/images/"
        for filename in os.listdir(pathFolder):
            _path_image_read = os.path.join(pathFolder, filename)
            if _path_image_read.lower().endswith(supported_formats):
                pics.append(_path_image_read)

        for pic in pics:
            pict = QtWidgets.QLabel(self)
            pict.setGeometry(col*200 +500, row*200 + 500, 400, 100)
            col+=1
            row+=1
            pict.setPixmap(QtGui.QPixmap(pic))

"""
"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Picasso Page Ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Multiple Page Starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
class Multiple(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Multiple, self).__init__(parent)
        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Multiple Page Ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Gif Page Starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
class Gif(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Gif, self).__init__(parent)
        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Gif Page Ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""



"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Main_Menu Starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


class Ui_Main_menu(QtWidgets.QMainWindow):
    def setupUi(self):
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.setObjectName("Main_menu")
        self.showFullScreen()
        self.setAutoFillBackground(False)
        self.setGeometry(0,0,width, height)
        self.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(0, 0, width, height)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem8 = QtWidgets.QSpacerItem(80, 80, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 6, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/gif_icon.jpeg'))
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setFlat(True)
        self.gridLayout.addWidget(self.pushButton_2, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/multiple_icon.jpeg'))
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setFlat(True)
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/picasso_icon.jpg'))
        self.pushButton_3.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_3.setFlat(True)
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 6, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Picasso\n Image Creator")
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("Multiple Shot\nCreator")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("Stop Motion\nCreator")
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 2, 1, 1)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.pushButton_2.clicked.connect(self.on_pushButton2_clicked)

        self.pushButton_3.clicked.connect(self.on_pushButton3_clicked)

    def on_pushButton_clicked(self):
        print("multiple")
        self.close()
        self.controller = Controller()
        self.controller.Multiple()


    def on_pushButton2_clicked(self):
        print("gif")
        self.close()
        self.controller = Controller()
        self.controller.Gif()


    def on_pushButton3_clicked(self):
        print("picasso")
        self.close()
        self.controller = Controller()
        self.controller.Picasso()

"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Main_menu ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Controller Starts

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


class Controller:

    def __init__(self):
        pass

    def Welcome(self):
        self.welcome = Welcome()
#        self.welcome.switch_window.connect(self.show_menu)
        self.welcome.show()

    def show_menu(self):
        self.welcome.close()
        self.ui = Ui_Main_menu()
        self.ui.setupUi()
        self.ui.show()

    def Picasso(self):
        self.Picasso = Picasso()
        self.Picasso.show()

    def Multiple(self):
        self.Multiple = Multiple()
        self.Multiple.show()

    def Gif(self):
        self.Gif = Gif()
        self.Gif.show()


"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Controller ends

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
mixer.init()

Splash = QtWidgets.QMainWindow()
controller = Controller()

ui = Ui_Splash()
ui.setupUi(Splash)
Splash.show()

progress = ThreadProgress()
progress.mysignal.connect(ui.progress)
progress.start()
#controller.show_menu()

sys.exit(app.exec_())
