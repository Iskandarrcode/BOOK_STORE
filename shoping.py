from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import mysql.connector as myc
import os

class Window(QMainWindow):
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
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ls = list()
        self.resize(1920, 1080)
        self.setFont(QFont("Montserrat", 14))
        self.setWindowTitle("Register")
        self.oyna = QWidget(self)
        self.oyna.setGeometry(0, 0, 1920, 1080)
        self.oyna.setStyleSheet("""
            background-color: rgb(102, 51, 153);""")

        self.lbl = QLabel(self)
        self.lbl.setText("WELCOME TO THE BOOKSTORE !")
        self.lbl.setFont(QFont("Montserrat", 30))
        self.lbl.setGeometry(550, 5, 800, 100)
        
        self.sqroll = QScrollArea(self)
        self.sqroll.setGeometry(330, 250, 1200, 700)
        self.sqroll.setStyleSheet("""
                background-color: rgb(147, 112, 219);
                border-radius: 22px;""")
        
        self.btn = QPushButton(self)
        self.btn.setFont(QFont("Montserrat", 20))
        self.btn.setStyleSheet("""
            background-color: rgb(102, 51, 153);
            border-radius: 22px;""")
        self.btn.setText("Name               Page               Price              Author")
        self.btn.setGeometry(420, 150, 1000, 40)

        self.lbl1 = QPushButton(self.sqroll)
        self.lbl2 = QPushButton(self.sqroll)
        self.lbl3 = QPushButton(self.sqroll)
        self.lbl4 = QPushButton(self.sqroll)
        self.lbl5 = QPushButton(self.sqroll)
        self.lbl6 = QPushButton(self.sqroll)
        self.lbl7 = QPushButton(self.sqroll)
        self.lbl8 = QPushButton(self.sqroll)
        self.lbl9 = QPushButton(self.sqroll)
        self.lbl10 = QPushButton(self.sqroll)
        self.lbl11 = QPushButton(self.sqroll)
        self.lbl12 = QPushButton(self.sqroll)
        self.lbl13 = QPushButton(self.sqroll)
        self.lbl14 = QPushButton(self.sqroll)
        self.lbl15 = QPushButton(self.sqroll)
    
        self.ls = [self.lbl1, self.lbl2, self.lbl3, self.lbl4, self.lbl5, self.lbl6, self.lbl7, self.lbl8, self.lbl9, self.lbl10, self.lbl11, self.lbl12, self.lbl13, self.lbl14, self.lbl15]

        self.lbl1.setFont(QFont("Montserrat", 20))
        self.lbl1.setGeometry(40, 10, 1100, 40)
        self.lbl2.setFont(QFont("Montserrat", 20))
        self.lbl2.setGeometry(40, 50, 1100, 40)
        self.lbl3.setFont(QFont("Montserrat", 20))
        self.lbl3.setGeometry(40, 90, 1100, 40)
        self.lbl4.setFont(QFont("Montserrat", 20))
        self.lbl4.setGeometry(40, 130, 1100, 40)
        self.lbl5.setFont(QFont("Montserrat", 20))
        self.lbl5.setGeometry(40, 170, 1100, 40)
        self.lbl6.setFont(QFont("Montserrat", 20))
        self.lbl6.setGeometry(40, 210, 1100, 40)
        self.lbl7.setFont(QFont("Montserrat", 20))
        self.lbl7.setGeometry(40, 250, 1100, 40)
        self.lbl8.setFont(QFont("Montserrat", 20))
        self.lbl8.setGeometry(40, 290, 1100, 40)
        self.lbl9.setFont(QFont("Montserrat", 20))
        self.lbl9.setGeometry(40, 330, 1100, 40)
        self.lbl10.setFont(QFont("Montserrat", 20))
        self.lbl10.setGeometry(40, 370, 1100, 40)
        self.lbl11.setFont(QFont("Montserrat", 20))
        self.lbl11.setGeometry(40, 410, 1100, 40)
        self.lbl12.setFont(QFont("Montserrat", 20))
        self.lbl12.setGeometry(40, 450, 1100, 40)
        self.lbl13.setFont(QFont("Montserrat", 20))
        self.lbl13.setGeometry(40, 490, 1100, 40)
        self.lbl14.setFont(QFont("Montserrat", 20))
        self.lbl14.setGeometry(40, 530, 1100, 40)
        self.lbl15.setFont(QFont("Montserrat", 20))
        self.lbl15.setGeometry(40, 570, 1100, 40)

        self.lbl1.clicked.connect(lambda : self.xisob(1))
        self.lbl2.clicked.connect(lambda : self.xisob(2))
        self.lbl3.clicked.connect(lambda : self.xisob(3))
        self.lbl4.clicked.connect(lambda : self.xisob(4))
        self.lbl5.clicked.connect(lambda : self.xisob(5))
        self.lbl6.clicked.connect(lambda : self.xisob(6))
        self.lbl7.clicked.connect(lambda : self.xisob(7))
        self.lbl8.clicked.connect(lambda : self.xisob(8))
        self.lbl9.clicked.connect(lambda : self.xisob(9))
        self.lbl10.clicked.connect(lambda : self.xisob(10))
        self.lbl11.clicked.connect(lambda : self.xisob(11))
        self.lbl12.clicked.connect(lambda : self.xisob(12))
        self.lbl13.clicked.connect(lambda : self.xisob(13))
        self.lbl14.clicked.connect(lambda : self.xisob(14))
        self.lbl15.clicked.connect(lambda : self.xisob(15))        
        
        
        self.chek_oyna = QLabel(self)
        self.chek_oyna.setFont(QFont("Calibri", 20, weight=100))
        self.chek_oyna.setGeometry(720, 900, 600, 50)
        self.chek_oyna.setStyleSheet(
            """text color: red;
                border-radius: 22px;"""
        )
       
        self.sum = 0
        self.dataa()
        
    def dataa(self, tb_name = "Bookss", db_name = "BOOKS"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        sorov = f"""Select Name, Page, Price, Author from {tb_name}"""
        cursor.execute(sorov)
        self.data = cursor.fetchall()
        con.commit()
        self.data2()
        
    def data2(self):
        for i in range(0, len(self.data)):
            book = str()
            for j in self.data[i]:
                book += str(j) + " "
            self.ls[i].setText(book)
            
        
    def xisob(self, text):
        if text == 1:
            self.sum += 85000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 2:
            self.sum += 150000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 3:
            self.sum += 1500000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 4:
            self.sum += 40000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 5:
            self.sum += 36000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 6:
            self.sum += 80000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 7:
            self.sum += 51000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 8:
            self.sum += 42000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 9:
            self.sum += 45000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 10:
            self.sum += 12000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 11:
            self.sum += 91000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 12:
            self.sum += 34000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 13:
            self.sum += 42000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 14:
            self.sum += 21000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 15:
            self.sum += 41000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")


class Database:
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
    
    def Create_table2(self, tb_name = "Orders", db_name = "BOOKS"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (Id int primary key auto_increment, User_id int, Units int)"""
        cursor.execute(sorov)
        con.commit()
        
    def Create_table3(self, tb_name = "Bookss", db_name = "BOOKS"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (Id int primary key auto_increment, Name varchar(60), Page int, Price int, Author varchar(60))"""
        cursor.execute(sorov)
        con.commit()
        
    def Insert_into2(self, User_id, Units):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "BOOKS")
        cursor = con.cursor()
        sql = "Insert into Orders (User_id, Units) values (%s, %s)"
        values = (User_id, Units)
        cursor.execute(sql, values)
        con.commit()
        
    def Insert_into3(self, Name, Page, Price, Author):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "BOOKS")
        cursor = con.cursor()
        sql = "Insert into Bookss (Name, Page, Price, Author) Values (%s, %s, %s, %s)"
        values = (Name, Page, Price, Author)
        cursor.execute(sql, values)
        con.commit()
        
        
db = Database()
db.Create_database("BOOKS")
db.Create_table1("Users")
db.Create_table2("Orders")
db.Create_table3("Bookss")

# db.Insert_into3("Xamsa", 1500, 85000, "Alisher Navoiy")
# db.Insert_into3("Atom odatlar", 300, 150000, "Jeyms Klir")
# db.Insert_into3("Molxona", 100, 15000, "Jorj Oruell")
# db.Insert_into3("Moliyaviy mustaqillik va erkin hayot sari", 236, 40000, "Devid Bax")
# db.Insert_into3("Zukkolar va landavurlar", 480, 36000, "Malkolm Gladuell")
# db.Insert_into3("Chalg'ituvchi dunyoda muvaffaqiyat sirlari", 230, 80000, "Kel Nyuport")
# db.Insert_into3("Ikki imperiya to'qnashuvi", 744, 51000, "Piter Hopkirk")
# db.Insert_into3("Murakkab sohaning sodda qiyofasi ", 540, 42000, "Charlz Uilan")
# db.Insert_into3("qudrat, farovonlik va kambag'allik manbalari", 676, 45000, "Daron Ajemo'g'li")                    
# db.Insert_into3("Savol ortidagi savol ", 104, 12000, "Jon G. Miller")
# db.Insert_into3("Stiv Jobs", 624, 91000, "Uolter Ayzekson")
# db.Insert_into3("Beparvolikning nozik san'ati ", 192, 34000, "Mark Menson")
# db.Insert_into3("Bir muhabbat tarixi ",496, 42000, "Devid Nikolls")
# db.Insert_into3("Qo'rqma", 368, 21000, "Javlon Jovliyev")
# db.Insert_into3("qudrat, farovonlik va kambag'allik manbalari", 676, 45000, "Daron Ajemo'g'li")