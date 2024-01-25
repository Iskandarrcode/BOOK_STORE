from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from shoping import Window
import mysql.connector as myc
import sys
import re

class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.__reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.resize(1920, 1080)
        self.setFont(QFont("Montserrat", 15))
        self.setWindowTitle("Register")
        self.oyna = QWidget(self)
        self.oyna.setGeometry(0, 0, 1920, 1080)
        self.oyna.setStyleSheet("""background-color: rgb(102, 51, 153)""")

        self.email = QLabel("Email", self)
        self.email.setGeometry(820, 250, 300, 30)
        self.line_email = QLineEdit(self)
        self.line_email.setGeometry(820, 290, 350, 40)
        self.mes_email = QLabel(self)
        self.mes_email.setGeometry(1200, 290, 150, 40)
        self.mes_email.setStyleSheet("color: red; font-size: 20px;")
        
        self.password = QLabel("Password", self)
        self.password.setGeometry(820, 370, 300, 30)
        self.line_password = QLineEdit(self)
        self.line_password.setGeometry(820, 410, 350, 40)
        self.mes_password = QLabel(self)
        self.mes_password.setGeometry(1200, 410, 150, 40)
        self.mes_password.setStyleSheet("color: red; font-size: 20px;")
        
        self.btn = QPushButton("Sabmit", self)
        self.btn.setGeometry(830, 530, 300, 50)
        self.btn.setStyleSheet("""background-color: rgb(102, 51, 153);
                                             border-radius: 22px;""")
        self.btn.clicked.connect(lambda : self.to_loginn())
        
        self.lbll = QLabel(self)
        self.lbll.setGeometry(820, 150, 300, 30)
        
    def Create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        cursor = con.cursor()
        cursor.execute(f"Create database if not exists {database_name}")
        con.commit()
    
    def Create_table1(self, tb_name = "Users", db_name = "BOOKS"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (Id int primary key auto_increment, Name varchar(60), Surname varchar(60), Email varchar(70), Password varchar(60))"""
        cursor.execute(sorov)
        con.commit()
        
    
    def to_loginn(self):
        self.lamp = True
        self.email = self.line_email.text().strip()
        self.password = self.line_password.text().strip()

     
        if not (re.fullmatch(self.__reg, self.email)):
            self.lamp = False
            self.mes_email.setText("invalid email")
        else:
            self.mes_email.setText("")
        
        if not (len(self.password) > 4):
            self.lamp = False

            self.mes_password.setText("invalid password")
        else:
            self.mes_password.setText("")
        
        if self.lamp:
            con = myc.connect(host="localhost", user="root", password="root", database="BOOKS")
            cursor = con.cursor()
            sql = f"SELECT * FROM Users WHERE Email = '{self.email}' AND Password = '{self.password}' "
            cursor.execute(sql)
            data = cursor.fetchall()
            con.commit()

            if len(data) == 1:
                self.oginn = Window()
                self.close()
                self.oginn.show()
            else:
                self.lbll.setText("Email yokiy Password xato !")
                self.line_email.setText("")
                self.line_password.setText("")
                