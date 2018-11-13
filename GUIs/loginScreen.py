from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QMessageBox,
    QLineEdit,
    QGridLayout
)
import pymysql
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)
import sys

class LoginScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.initLoginScreen()

    def initLoginScreen(self):

        ## create layouts
        self.vLayout = QVBoxLayout(self)
        self.buttonRow = QHBoxLayout(self)
        self.grid = QGridLayout(self)

        self.emailLabel = QLabel('Email: ', self)
        self.passwordLabel = QLabel('Password: ', self)

        self.emailLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)

        self.loginButton = QPushButton('Login', self)
        self.loginButton.resize(75, 32)
        self.registrationButton = QPushButton('Registration', self)
        self.registrationButton.resize(75, 32)

        # Sets the buttons to be not enabled until all the fields are entered
        self.loginButton.setEnabled(False)
        self.emailLineEdit.textChanged.connect(self.checkFields)
        self.passwordLineEdit.textChanged.connect(self.checkFields)


        self.grid.addWidget(self.emailLabel, 0, 0)
        self.grid.addWidget(self.emailLineEdit, 0, 1)
        self.grid.addWidget(self.passwordLabel, 2, 0)
        self.grid.addWidget(self.passwordLineEdit, 2, 1)

        self.buttonRow.addWidget(self.loginButton)
        self.buttonRow.addWidget(self.registrationButton)

        self.vLayout.addLayout(self.grid)
        self.vLayout.addLayout(self.buttonRow)

        self.setLayout(self.vLayout)


        self.title = 'User Login'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def checkFields(self):
        if len(self.emailLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0:
            self.loginButton.setEnabled(True)
        if not(len(self.emailLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0):
            self.loginButton.setEnabled(False)

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = LoginScreen()
    main.show()
    sys.exit(app.exec_())
