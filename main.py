import sys
from tkinter import NO
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
from pymongo import MongoClient
import uuid

client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("main_window.ui", self)
        self.setWindowTitle("Food Lover")

        self.login_btn.clicked.connect(self.Attempt_Login)
        self.register_btn.clicked.connect(self.register)
        self.surf_btn.clicked.connect(self.Surf)


    def Attempt_Login(self):

        email = self.main_email_entry.text()
        password = self.main_pw_entry.text()

        if email == "" or password == "":
            self.login_error.setText("Please enter a valid email and password!")
            return
        
        user_data = db['login_data']
        user = user_data.find_one({"email": email})

        if user: # if user exists checks password and acc type, opening the appropriate window

            if user["password"] == password: 
                if user["type"] == "customer":
                    self.customer_login = UserLogin(email)
                    self.customer_login.show()
                    self.close()
                
                elif user["type"] == "store": # store account opens a new window for workers
                    self.store_login = StoreLogin()
                    self.store_login.show()
                    self.close()


            else:
                self.login_error.setText("Password is incorrect!")
        
        else:
            self.login_error.setText("User not found!") 


    def register(self): # opens register window while closing the main one
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

    def Surf(self):
        print("OHHH YEAHHHHH")

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("register_window.ui", self)
        self.setWindowTitle("Register")

        self.back_btn.clicked.connect(self.register_bck_btn)
        self.reg_btn.clicked.connect(self.RegisterUser)

    def register_bck_btn(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def RegisterUser(self):
        name = self.name_reg.text()
        email = self.email_reg.text()
        pw = self.pw_reg.text()
        deposit = self.init_deposit.text()

        if email == "" or pw == "" or name == "" or deposit == "":
            self.reg_error.setText("Please enter valid credentials!")
            return

        if not(deposit.isnumeric()):
            self.reg_error.setText("Please use numbers for deposit")
            return
    
        user_data = db['login_data']

        if user_data.find_one({'email': email}):
            self.reg_error.setText("User already exists")
        else:
            new_user = {
                "name": name,
                "email": email,
                "password": pw,
                "type": "customer",
                "complaints": 0,
                "deposit": 0
            }
            user_data.insert_one(new_user)
            
            #return to main window
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
            


class UserLogin(QMainWindow): # succesful user login window
    def __init__(self, user):
        super().__init__()
        uic.loadUi("search_browse.ui", self)
        self.setWindowTitle("Food Lover")
        
        user_data = db['login_data']
        user_info = user_data.find_one({"email": user})
        food_data = db['food']

        if user_info:
            # Update QLabel with user name
            self.name.setText(user_info["name"])

            # Create a standard item model
            self.model = QStandardItemModel()

            # Get all food items from the database
            food_items = food_data.find()

            # Add each food item to the model
            for food_item in food_items:
                item = QStandardItem(str(food_item))
                self.model.appendRow(item)

            # Set the model for the column view
            self.columnView.setModel(self.model)

        def filterFoodItems():
            # Get the search text
            search_text = self.textInput.text()

            # Clear the model
            self.model.clear()

            # Get all food items from the database that match the search text
            food_items = food_data.find({"$text": {"$search": search_text}})

            # Add each matching food item to the model
            for food_item in food_items:
                item = QStandardItem(str(food_item))
                self.model.appendRow(item)

            # Set the model for the column view
            self.columnView.setModel(self.model)
        

        # Connect search button to filter function
        self.searchButton.clicked.connect(filterFoodItems)

        
        
        
        

                        
        
class StoreLogin(QMainWindow): # store login that has access to all the different functions for workers
    def __init__(self):
        super().__init__()
        uic.loadUi("store_main.ui", self)
        self.setWindowTitle("Food Lover")

        self.manager_btn.clicked.connect(self.manager_login)
        # self.chef_btn.clicked.connect(self.chef_login)
        # self.delivery_btn.clicked.connect(self.deliver_login)
        # self.importer_btn.clicked.connect(self.importer_login)

    def getID(self):
        text, dialog = QInputDialog.getText(self, "ID", "Enter your ID:")
        return text
    
    def manager_login(self):
        employee_id = self.getID()
        if employee_id == "1214": # this will be the managers ID
            self.manager_win = ManagerWindow()
            self.manager_win.show()
            self.close()
        else:
            QMessageBox.information(self, "Information", "ID is incorrect")

# handles all the managers functions
class ManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("manager.ui", self)
        self.setWindowTitle("Manager Menu")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())