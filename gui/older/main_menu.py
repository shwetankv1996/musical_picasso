# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_designed.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_menu(object):
    def setupUi(self, Main_menu):
        Main_menu.setObjectName("Main_menu")
        Main_menu.resize(928, 682)
        Main_menu.setAutoFillBackground(False)
        Main_menu.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.centralwidget = QtWidgets.QWidget(Main_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setIcon(QtGui.QIcon('/home/sv-v1/projects/picasso/images/gif_icon.jpeg'))
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(155, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(156, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(156, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(155, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Main_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_menu)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 22))
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
        self.pushButton_3.setText(_translate("Main_menu", "Picasso"))
        self.pushButton.setText(_translate("Main_menu", "multiple"))
        self.pushButton_2.setText(_translate("Main_menu", "gif"))
        self.label_2.setText(_translate("Main_menu", "Multiple Shot Capture"))
        self.label_3.setText(_translate("Main_menu", "Create Stop Motion"))
        self.label.setText(_translate("Main_menu", "Picasso Image Creator"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_menu = QtWidgets.QMainWindow()
    ui = Ui_Main_menu()
    ui.setupUi(Main_menu)
    Main_menu.show()
    sys.exit(app.exec_())
