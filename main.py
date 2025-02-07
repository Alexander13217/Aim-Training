from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow
import sys
import random

app = QtWidgets.QApplication(sys.argv)


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.circle1.hide()
ui.circle2.hide()
ui.circle3.hide()
ui.circle4.hide()
ui.circle5.hide()
ui.click_info.hide()
ui.info_label.hide()
ui.click_on.hide()
ui.time_left.hide()
MainWindow.show()

timer = QtCore.QTimer()
timer.setInterval(1000)
count_time = 15
count_click = 0
def start():
    global count_time
    count_time = 15
    
    ui.label_2.hide()
    ui.start_bt.hide()
    ui.circle1.show()
    ui.circle2.show()
    ui.circle3.show()
    ui.circle4.show()
    ui.circle5.show()
    ui.click_info.show()
    ui.info_label.show()
    ui.click_on.show()
    ui.time_left.show()
    timer.start()

def stop():
    ui.circle1.hide()
    ui.circle2.hide()
    ui.circle3.hide()
    ui.circle4.hide()
    ui.circle5.hide()
    ui.start_bt.show()
    ui.start_bt.setText('Next')

def next():
    ui.click_on.hide()
    ui.time_left.hide()
    ui.info_label.hide()
    ui.click_info.hide()
    ui.label_2.show()
    ui.start_bt.setText('START')

def on_click():
    if ui.start_bt.text() == 'Next':
        next()
    elif ui.start_bt.text() == 'START':
        start()
    
def circle1():
    global count_click
    ui.circle1.hide()
    w =  random.randint(10,640)
    y =  random.randint(10,440)
    ui.circle1.setGeometry(QtCore.QRect(w, y, 90, 90))
    ui.circle1.show()
    count_click += 1
    ui.click_on.setText(str(count_click))
def circle2():
    global count_click
    count_click += 1
    ui.click_on.setText(str(count_click))
    ui.circle2.hide()
    w =  random.randint(10,640)
    y =  random.randint(10,440)
    ui.circle2.setGeometry(QtCore.QRect(w, y, 90, 90))
    ui.circle2.show()

def circle3():
    global count_click
    count_click += 1
    ui.click_on.setText(str(count_click))
    ui.circle3.hide()
    w =  random.randint(10,640)
    y =  random.randint(10,440)
    ui.circle3.setGeometry(QtCore.QRect(w, y, 90, 90))
    ui.circle3.show()

def circle4():
    global count_click
    count_click += 1
    ui.click_on.setText(str(count_click))
    ui.circle4.hide()
    w =  random.randint(10,640)
    y =  random.randint(10,440)
    ui.circle4.setGeometry(QtCore.QRect(w, y, 90, 90))
    ui.circle4.show()

def circle5():
    global count_click
    count_click += 1
    ui.click_on.setText(str(count_click))
    ui.circle5.hide()
    w =  random.randint(10,640)
    y =  random.randint(10,440)
    ui.circle5.setGeometry(QtCore.QRect(w, y, 90, 90))
    ui.circle5.show()

def time():
    global count_time

    if count_time > 0:     
        ui.time_left.setText(str(count_time))
        count_time -= 1
    else:
        timer.stop()
        stop()


ui.circle5.clicked.connect(circle5)
ui.circle4.clicked.connect(circle4)
ui.circle3.clicked.connect(circle3)    
ui.circle2.clicked.connect(circle2)
ui.circle1.clicked.connect(circle1)
ui.start_bt.clicked.connect(on_click)
timer.timeout.connect(time)
sys.exit(app.exec_())