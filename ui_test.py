import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import QtGui
from pymongo import MongoClient

client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("manager.ui", self)

        workers = db['workers']
        usr_manager = workers.find_one({'position': 'Manager'})
        self.welcome_manager_txt.setText("Welcome, " + usr_manager['name']) # type: ignore

        self.wages_btn.clicked.connect(self.wages)

    def wages(self):
        self.wage_win = Wages()
        self.wage_win.show()


class Wages(QMainWindow):
    def __init__(self):
        super(Wages, self).__init__()
        uic.loadUi("wages.ui", self)
        self.setWindowTitle("Wages")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window.show()
    sys.exit(app.exec_())