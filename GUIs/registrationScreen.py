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

class RegistrationScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.initRegistrationScreen()

    def initRegistrationScreen(self):

        ## create layouts
        self.vLayout = QVBoxLayout(self)
        self.buttonRow = QHBoxLayout(self)
        self.grid = QGridLayout(self)

        self.emailLabel = QLabel('Email: ', self)
        self.userNameLabel = QLabel('Username: ', self)
        self.passwordLabel = QLabel('Password: ', self)
        self.confirmPasswordLabel = QLabel('Confirm Password: ', self)

        self.emailLineEdit = QLineEdit(self)
        self.userNameLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)
        self.confirmPasswordLineEdit = QLineEdit(self)

        self.registerVisitorButton = QPushButton('Register Visitor', self)
        self.registerVisitorButton.resize(75, 32)
        self.registerStaffButton = QPushButton('Register Staff', self)
        self.registerStaffButton.resize(75, 32)

        # Sets the buttons to be not enabled until all the fields are entered
        self.registerVisitorButton.setEnabled(False)
        self.registerStaffButton.setEnabled(False)
        self.emailLineEdit.textChanged.connect(self.checkFields)
        self.userNameLineEdit.textChanged.connect(self.checkFields)
        self.passwordLineEdit.textChanged.connect(self.checkFields)
        self.confirmPasswordLineEdit.textChanged.connect(self.checkFields)


        self.grid.addWidget(self.emailLabel, 0, 0)
        self.grid.addWidget(self.emailLineEdit, 0, 1)
        self.grid.addWidget(self.userNameLabel, 1, 0)
        self.grid.addWidget(self.userNameLineEdit, 1, 1)
        self.grid.addWidget(self.passwordLabel, 2, 0)
        self.grid.addWidget(self.passwordLineEdit, 2, 1)
        self.grid.addWidget(self.confirmPasswordLabel, 3, 0)
        self.grid.addWidget(self.confirmPasswordLineEdit, 3, 1)

        self.buttonRow.addWidget(self.registerVisitorButton)
        self.buttonRow.addWidget(self.registerStaffButton)

        self.vLayout.addLayout(self.grid)
        self.vLayout.addLayout(self.buttonRow)

        self.setLayout(self.vLayout)


        self.title = 'User Registration'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def checkFields(self):
        if len(self.emailLineEdit.text()) > 0 and len(self.userNameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0 and len(self.confirmPasswordLineEdit.text()) > 0:
            self.registerVisitorButton.setEnabled(True)
            self.registerStaffButton.setEnabled(True)
        if not(len(self.emailLineEdit.text()) > 0 and len(self.userNameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0 and len(self.confirmPasswordLineEdit.text()) > 0):
            self.registerVisitorButton.setEnabled(False)
            self.registerStaffButton.setEnabled(False)

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = RegistrationScreen()
    main.show()
    sys.exit(app.exec_())
