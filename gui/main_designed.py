# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu_designed.ui'
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(120, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(120, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(121, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(121, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
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
        self.pushButton_2.setText(_translate("Main_menu", "gif"))
        self.label_3.setText(_translate("Main_menu", "TextLabel"))
        self.pushButton_3.setText(_translate("Main_menu", "Picasso"))
        self.label_2.setText(_translate("Main_menu", "TextLabel"))
        self.label.setText(_translate("Main_menu", "TextLabel"))
        self.pushButton.setText(_translate("Main_menu", "multiple"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_menu = QtWidgets.QMainWindow()
    ui = Ui_Main_menu()
    ui.setupUi(Main_menu)
    Main_menu.show()
    sys.exit(app.exec_())
