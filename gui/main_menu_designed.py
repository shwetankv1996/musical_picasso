# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_menu(object):
    def setupUi(self, Main_menu):
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        Main_menu.setObjectName("Main_menu")
        Main_menu.resize(800, 600)
        Main_menu.setAutoFillBackground(False)
        Main_menu.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.centralwidget = QtWidgets.QWidget(Main_menu)
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
        self.pushButton_2.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/picasso_icon.jpg'))
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton_2, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/gif_icon.jpg'))
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/multiple_shot_icon.jpg'))
        self.pushButton_3.setIconSize(QtCore.QSize(200, 200))
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 6, 1, 1)
        Main_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_menu)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Main_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_menu)
        self.statusbar.setObjectName("statusbar")
        Main_menu.setStatusBar(self.statusbar)

        self.retranslateUi(Main_menu)
        QtCore.QMetaObject.connectSlotsByName(Main_menu)

    def retranslateUi(self, Main_menu):
        _translate = QtCore.QCoreApplication.translate
        Main_menu.setWindowTitle(_translate("Main_menu", "MainWindow"))
        self.pushButton_2.setText(_translate("Main_menu", "gif"))
        self.pushButton.setText(_translate("Main_menu", "multiple"))
        self.pushButton_3.setText(_translate("Main_menu", "Picasso"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_menu = QtWidgets.QMainWindow()
    ui = Ui_Main_menu()
    ui.setupUi(Main_menu)
    Main_menu.show()
    sys.exit(app.exec_())
