
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import os
import sys
import time


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

FROM_SPLASH,_ = uic.loadUiType(os.path.join(os.path.dirname(__file__),"splash.ui"))
FROM_MAIN,_ = uic.loadUiType(os.path.join(os.path.dirname(__file__),"main.ui"))


class Main(QtWidgets.QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        QtWidgets.QMessageBox.information(self, "Omar Othman", "This code writed by Omar Othman")

        
class Splash(QtWidgets.QMainWindow, FROM_SPLASH):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        pixmap = QtGui.QPixmap("/home/sv-v1/projects/picasso/images/Musical Picasso 1.png")
        self.splah_image.setPixmap(pixmap.scaled(350, 300))
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
        
    @QtCore.pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 100:
            self.hide()
            main = Main(self)
            main.show()


class Controller:

    def __init__(self):
        pass

    def show_splash(self):
        self.splash = Splash()
        self.splash.switch_window.connect(self.show_main)
        self.splash.show()

    def show_main(self):
        self.window = Main()
#        self.window.switch_window.connect(self.show_window_two)
        self.splash.close()
        self.window.show()



if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_splash()
    sys.exit(app.exec_())

