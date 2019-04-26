# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spash.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splash(object):
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.showFullScreen()
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
        self.label.setPixmap(QtGui.QPixmap("../../images/Musical Picasso.png"))
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
        self.progressBar.setProperty("value", 0)
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

#        self.retranslateUi(Splash)
#        QtCore.QMetaObject.connectSlotsByName(Splash)

#    def retranslateUi(self, Splash):
#        _translate = QtCore.QCoreApplication.translate
#        Splash.setWindowTitle(_translate("Splash", "MainWindow"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Splash = QtWidgets.QMainWindow()
    ui = Ui_Splash()
    ui.setupUi(Splash)
    Splash.show()
    sys.exit(app.exec_())
