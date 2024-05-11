import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("store_main.ui", self)
        self.manager_btn.clicked.connect(self.test)

    def test(self):
        text, ok = QInputDialog.getText(self, "ID", "Enter your ID:")
        if ok:
            QMessageBox.information(self, "Information", f'Hello, {text}!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window.show()
    sys.exit(app.exec_())