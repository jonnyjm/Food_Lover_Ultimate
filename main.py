import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
from pymongo import MongoClient

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
                    self.customer_login = UserLogin()
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

        if email == "" or pw == "" or name == "":
            self.reg_error.setText("Please enter valid credentials!")
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
                "status": "regular",
                "complaints": 0,
                "deposit": 0
            }
            user_data.insert(new_user)


class UserLogin(QMainWindow): # succesful user login window
    def __init__(self):
        super().__init__()
        uic.loadUi("user_main.ui", self)
        self.setWindowTitle("Food Lover")                
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("food_lover.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())