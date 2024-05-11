import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("user_main.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())