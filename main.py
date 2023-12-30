from PyQt5. QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setStyleSheet('Background-color:whitesmoke; font-size:24px; padding:5px;color: goldenrod; font-family: ARIAL BLACK')
win.resize(1200,700)
win.setWindowTitle('EasyEditor')

btn_dir = QPushButton('Папка')
btn_dir.setCursor(Qt.PointingHandCursor)
btn_dir.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
lb_files = QListWidget()
btn_left = QPushButton('Вліво')
btn_left.setCursor(Qt.PointingHandCursor)
btn_left.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
btn_right = QPushButton('Вправо')
btn_right.setCursor(Qt.PointingHandCursor)
btn_right.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
btn_mirrow = QPushButton('Відзеркалення')
btn_mirrow.setCursor(Qt.PointingHandCursor)
btn_mirrow.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
btn_sharp = QPushButton('Різкість')
btn_sharp.setCursor(Qt.PointingHandCursor)
btn_sharp.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
btn_bw = QPushButton('Ч/Б')
btn_bw.setCursor(Qt.PointingHandCursor)
btn_bw.setStyleSheet('border: 2px solid silver; border-radius: 20px; background-color: lightgray')
lb_image = QLabel('Картинка')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lb_files)
col2.addWidget(lb_image)
col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_mirrow)
col3.addWidget(btn_sharp)
col3.addWidget(btn_bw)
row.addLayout(col1,20)
row.addLayout(col2,60)
row.addLayout(col3,20)
win.setLayout(row)

win.show()
app.exec_()
