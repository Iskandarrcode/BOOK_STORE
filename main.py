from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from register import Register
from login import Login
import sys


class Asosiy(QMainWindow):
    def  __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon("stack-of-books.ico"))
        self.oyna = QWidget()
        self.resize(1920, 1080)
        self.setWindowTitle("Book store")
        self.setStyleSheet("background-color: rgb(147, 112, 219)")


        self.mainver = QVBoxLayout()
        self.labelver = QHBoxLayout()
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setText("Book store")
        self.lbl.setStyleSheet("color: white")
        self.lbl.setFont(QFont("Montserrat", 50))



        self.mainver.addStretch()
        self.labelver.addWidget(self.lbl)
        self.mainver.addLayout(self.labelver)

        self.btnhor = QHBoxLayout()
        self.btnhor.setAlignment(Qt.AlignCenter)

        self.btnlog = QPushButton("      Login      ")
        self.btnlog.setStyleSheet("""background-color: #D4DEE5;
                             border-radius: 10px;
                             border: 2px;""")
        self.btnlog.setFont(QFont("Montserrat", 25))


        self.btnreg = QPushButton("    Register    ")
        self.btnreg.setStyleSheet("""background-color: #D4DEE5;
                             border-radius: 10px;
                             border: 2px;""")
        self.btnreg.setFont(QFont("Montserrat", 25))

        self.metalbl = QLabel("Meta © 2024")
        self.metalbl.setAlignment(Qt.AlignCenter)
        self.metalbl.setStyleSheet("""color: white;""")
        self.metalbl.setFont(QFont("Montserrat", 15))

        self.metahor = QHBoxLayout()
        self.metahor.addWidget(self.metalbl)

        self.btnhor.addStretch()
        self.btnhor.addStretch()

        self.btnhor.addWidget(self.btnlog)
        self.btnhor.addStretch()
        self.btnhor.addWidget(self.btnreg)
        self.btnhor.addStretch()
        self.btnhor.addStretch()

        self.mainver.addLayout(self.btnhor)
        self.mainver.addStretch()

        self.mainver.addLayout(self.metahor)
        self.oyna.setLayout(self.mainver)
        self.setCentralWidget(self.oyna)

        self.btnreg.clicked.connect(lambda: self.register())
        self.btnlog.clicked.connect(lambda: self.login())



    def login(self):
        self.login = Login()
        self.close()
        self.login.show()


    def register(self):
        self.register = Register()
        self.close()
        self.register.show()



app = QApplication([])
dastur = Asosiy()
dastur.show()
sys.exit(app.exec_())