from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time

supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.dib', '.jpe', '.jp2', '.pgm', '.tiff', '.tif', '.ppm')



class Picasso(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Picasso, self).__init__(parent)
        self.setWindowTitle('Picasso Image Creator')
#        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.setGeometry(0,0,width, height)

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



class Multiple(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Multiple, self).__init__(parent)
        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")


class Gif(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Gif, self).__init__(parent)
        self.showFullScreen()
        self.setStyleSheet("background-color: rgb(49, 54, 59);")



class Controller:

    def __init__(self):
        pass

    def Picasso(self):
        self.Picasso = Picasso()
        self.Picasso.show()

    def Multiple(self):
        self.Multiple = Multiple()
        self.Multiple.show()

    def Gif(self):
        self.Gif = Gif()
        self.Gif.show()



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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/gif_icon.jpeg'))
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton_2, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/multiple_icon.jpeg'))
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/picasso_icon.jpg'))
        self.pushButton_3.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 6, 1, 1)
        self.setCentralWidget(self.centralwidget)

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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#    Main_menu = QtWidgets.QMainWindow()
    ui = Ui_Main_menu()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
