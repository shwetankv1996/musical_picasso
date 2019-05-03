import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class main_menu(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		screen_resolution = app.desktop().screenGeometry()
		width, height = screen_resolution.width(), screen_resolution.height()
		btn_y_line = height / 4
		btn_x_line = width - 600
		print(width, "\t", height, "\t", btn_x_line)
		self.setBackgroundRole(QPalette.Base)
		self.setStyleSheet("background-color: rgb(49, 54, 59);")
		self.setGeometry(0, 0, width, height)
		self.button1 = QPushButton('',self)
		self.button1.setIcon(QIcon('/home/sv-v1/projects/picasso/images/picasso_icon.jpg'))
		self.button1.setIconSize(QSize(200, 200))
		self.button1.move(btn_x_line/4,btn_y_line)
#		layout1 = QVBoxLayout(self)
#		layout1.addWidget(self.button1)
		self.button2 = QPushButton('',self)
		self.button2.setIcon(QIcon('/home/sv-v1/projects/picasso/images/multiple_shot_icon.jpeg'))
		self.button2.setIconSize(QSize(200, 200))
		self.button2.move(width/2 - 100,btn_y_line)
#		layout2 = QVBoxLayout(self)
#		layout2.addWidget(self.button2)
		self.button3 = QPushButton('',self)
		self.button3.setIcon(QIcon('/home/sv-v1/projects/picasso/images/gif_icon.jpeg'))
		self.button3.setIconSize(QSize(200, 200))
		self.button3.move(btn_x_line,btn_y_line)
#		layout3 = QVBoxLayout(self)
#		layout3.addWidget(self.button3)
		grid = QGridLayout()
		layout = QVBoxLayout(self)
		btn_layout = QHBoxLayout()
		# !!!
		self.spacer1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.spacer2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.spacer3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
		grid.addItem(self.spacer1, 1, 0)
		grid.addWidget(self.button1, 1, 1)
		grid.addItem(self.spacer2, 1, 2)
		grid.addWidget(self.button2, 1, 3)
		grid.addItem(self.spacer3, 1, 4)
		grid.addWidget(self.button3, 1, 5)
		self.setLayout(grid)
"""
		btn_layout.addItem(self.spacer1,1)
		btn_layout.addWidget(self.button1,2)
		btn_layout.addItem(self.spacer2,3)
		btn_layout.addWidget(self.button2, 4)
		btn_layout.addItem(self.spacer3,5)
		btn_layout.addWidget(self.button3,6)
		layout.addLayout(btn_layout)
"""

app = QApplication(sys.argv)
a = main_menu()
a.show()
sys.exit(app.exec_())
