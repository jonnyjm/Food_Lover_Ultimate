# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jonny\OneDrive\Documents\Food_Lover_Ultimate\store_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 160, 481, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manager_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manager_btn.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 25px solid;")
        self.manager_btn.setObjectName("manager_btn")
        self.verticalLayout.addWidget(self.manager_btn)
        self.chef_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chef_btn.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 25px solid")
        self.chef_btn.setObjectName("chef_btn")
        self.verticalLayout.addWidget(self.chef_btn)
        self.delivery_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delivery_btn.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 25px solid")
        self.delivery_btn.setObjectName("delivery_btn")
        self.verticalLayout.addWidget(self.delivery_btn)
        self.importer_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.importer_btn.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 25px solid")
        self.importer_btn.setObjectName("importer_btn")
        self.verticalLayout.addWidget(self.importer_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 540, 801, 21))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 801, 130))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\jonny\\OneDrive\\Documents\\Food_Lover_Ultimate\\Images/food_lover.ico"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.manager_btn.setText(_translate("MainWindow", "Manager Menu"))
        self.chef_btn.setText(_translate("MainWindow", "Chef Menu"))
        self.delivery_btn.setText(_translate("MainWindow", "Delivery Menu"))
        self.importer_btn.setText(_translate("MainWindow", "Importer Menu"))
        self.label.setText(_translate("MainWindow", "Copyright: Group F"))
