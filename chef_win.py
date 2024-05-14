import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import random
from pymongo import MongoClient

client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']
menu = db['food']
workers = db['workers']
complaint_db = db['worker_complaints']
class ChefWin(QMainWindow):
    def __init__(self):
        super(ChefWin, self).__init__()
        uic.loadUi("chef.ui", self)
        self.setWindowTitle("Chef Menu")

        self.menu()

        self.add_btn.clicked.connect(self.addFood)
        self.refresh.clicked.connect(self.menu)
        self.remove_btn.clicked.connect(self.remove)
        self.file_complain.clicked.connect(self.complain)

    def remove(self):
        userID = self.id_num.text()
        if userID == "":
            self.error_label.setText("Enter a valid ID number")
            return
        chef = workers.find_one({'passID': userID})
        if chef and chef['position'] == 'Chef':
            removed_item, dialog = QInputDialog.getText(self, "Remove item", "Enter name of item to be removed:")
            item = menu.find_one({'name': removed_item})
            if item:
                if item['chefId'] != userID:
                    QMessageBox.information(self, "Information", "Can't remove another chef's item")
                else:
                    menu.find_one_and_delete({'name': removed_item})
                    QMessageBox.information(self, "Information", "Item removed succesfully!")
                    self.menu

            else:
                QMessageBox.information(self, "Information", "Item not found")
        else:
            self.error_label.setText("Only chef's can remove items")


    def menu(self):
        data = list(menu.find())

        self.menu_table.setRowCount(len(data))
        for row, item in enumerate(data):
            name_item = QTableWidgetItem(item["name"])
            desc_item = QTableWidgetItem(item['description'])
            rating_item = QTableWidgetItem(str(item['averageRating']))
            id_item = QTableWidgetItem(item["chefId"])
            num_item = QTableWidgetItem(item['numRatings'])

            self.menu_table.setItem(row, 0, name_item)
            self.menu_table.setItem(row, 3, id_item)
            self.menu_table.setItem(row, 2, num_item)
            self.menu_table.setItem(row, 1, rating_item)
            self.menu_table.setItem(row, 4, desc_item)
    
    def addFood(self):
        id_num = self.id_num.text()
        chef = workers.find_one({'passID': id_num})
        if chef and chef['position'] == 'Chef':
            self.food = foodAdd(id_num)
            self.food.show()
            self.error_label.setText("")
        else:
            self.error_label.setText("Invalid ID")
            return
    
    def complain(self):
        id_num = self.id_num.text()
        chef = workers.find_one({'passID': id_num})
        if chef and chef['position'] == 'Chef':
            self.complaint = CheftoImporterComplaint(id_num)
            self.complaint.show()
            self.error_label.setText("")
        else:
            self.error_label.setText("Invalid ID")
            return
        
class CheftoImporterComplaint(QMainWindow):
    def __init__(self, ident):
        super(CheftoImporterComplaint, self).__init__()
        uic.loadUi("chef_to_importer_complaint.ui", self)
        
        self.complainer_id = ident
        self.send_btn.clicked.connect(self.send)

    def send(self):
        name = self.importer_name.text()
        complain = self.complaint_text.toPlainText()
        if name == 'Joe':
            self.err_msg.setText("That's the manager !")
            return
        
        if name != '' and complain != "":
            worker = workers.find_one({'name': name})
        else: 
            return

        if self.quality.isChecked():
            tipo = 'Quality'
        else:
            tipo = 'Fraud'
        if worker:
            if worker['position'] == 'Importer':
                from_worker = workers.find_one({'passID': self.complainer_id})
                from_name = from_worker['name'] # type: ignore
                complaint_db.insert_one({
                    'from':  from_name,
                    'fromID': self.complainer_id,
                    'to': str(worker['name']),
                    'toID': str(worker["passID"]),
                    'complaint': complain,
                    'type': tipo,
                    'approved': 'N/A',
                    'complaintID': str(random.randint(0,2000))
                })
            
            else:
                self.err_msg.setText("Worker not an Importer")
        
        else:
            self.err_msg.setText("Worker not found")



class foodAdd(QMainWindow):
    def __init__(self, ident):
        super(foodAdd, self).__init__()
        uic.loadUi("add_food.ui", self)
        self.keywords = []
        self.add_kword.clicked.connect(self.addkword)
        self.add_food.clicked.connect(self.addFood)
        self.idd = ident

    def addkword(self):
        text = self.kword.text()
        if text != "":
            self.keywords.append(text)
        else:
            return
    
    def addFood(self):
        name = self.food_name.text()
        desc = self.description.toPlainText()
        if name != "" and desc != "":
            menu.insert_one({
                'name': name,
                'description': desc,
                'keywords': self.keywords,
                'averageRating': 0,                
                'chefId': self.idd,
                'numRatings': '0'
            })
            QMessageBox.information(self, "Information", "Food was succesfuly added!")
            self.close()


            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChefWin()
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window.show()
    sys.exit(app.exec_())
        