import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
from pymongo import MongoClient

client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']
workers = db['workers']

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("manager.ui", self)
        manager = workers.find_one({'position': 'Manager'})
        self.welcome_manager_txt.setText("Welcome, " + manager['name']) # type: ignore
        self.loadData()

        self.change_wage.clicked.connect(self.changeWage)
        self.fire_btn.clicked.connect(self.fireEMPL)
        self.hire_btn.clicked.connect(self.hire)
        self.refresh.clicked.connect(self.loadData)

    def loadData(self):
        data = list(workers.find())

        self.worker_table.setRowCount(len(data))
        for row, item in enumerate(data):
            name_item = QTableWidgetItem(item["name"])
            wage_item = QTableWidgetItem("$" + item["wage"])
            id_item = QTableWidgetItem(item["passID"])
            position_item = QTableWidgetItem(item['position'])
            rating_item = QTableWidgetItem(item['rating'])

            self.worker_table.setItem(row, 0, position_item)
            self.worker_table.setItem(row, 1, name_item)
            self.worker_table.setItem(row, 2, id_item) 
            self.worker_table.setItem(row, 3, wage_item)
            self.worker_table.setItem(row, 4, rating_item)
    
    def changeWage(self):
        userID = self.id_num.text()
        if userID == "1214":
            self.error_label.setText("Can't change Manager wages")
            return
        elif userID == "":
            self.error_label.setText("Please enter valid ID")
        elif workers.find_one({'passID': userID}):
            new_wage, dialog = QInputDialog.getText(self, "Set New Wage", "Enter new Wages:")
            workers.update_one(
                {'passID':userID},
                {"$set": {'wage': new_wage}}
            )
            self.loadData()
        else:
            self.error_label.setText("Worker ID not found")

    def fireEMPL(self):
        userID = self.id_num.text()
        if userID == "1214":
            self.error_label.setText("Can't fire Manager")
            return
        elif userID == "":
            self.error_label.setText("Please enter valid ID")
            return
        elif workers.find_one({'passID': userID}):
            workers.find_one_and_delete({'passID': userID})
            self.loadData()
            return
        else:
            self.error_label.setText("User not found")

    def hire(self):
        self.hiring = Hiring()
        self.hiring.show()

class Hiring(QMainWindow):
    def __init__(self):
        super(Hiring, self).__init__()
        uic.loadUi("hire_employee.ui", self)
        self.setWindowTitle("Hiring...")
        self.setFocus()

        self.btn.clicked.connect(self.Hire)

    def Hire(self):
        name = self.name.text()
        position = self.position.text()
        wage = self.pay.text()
        id = self.ident.text()

        if name == "" or wage == "" or not(wage.isnumeric()) or id == "" or not(id.isnumeric()):
            self.err_label.setText("Please fill in valid credentials")
            return
        
        if workers.find_one({'passID': id}):
            self.err_label.setText("ID already exists")
            return

        if position == "Chef" or position == "Delivery" or position == "Importer":
            workers.insert_one({
                'name': name,
                'position': position,
                'wage': wage,
                'passID': id,
                'rating': 'N/A'
            })
            self.err_label.setText("Success")
            self.close()
        else:
            self.err_label.setText("This position doesn't exist")
            



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window.show()
    sys.exit(app.exec_())