import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout
)
import pymysql
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)

from loginScreen import LoginScreen

class AdministratorFunctionality(QWidget):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__()

        self.initAdministratorFunctionality()

    def initAdministratorFunctionality(self):

        self.grid = QGridLayout()

        #create buttons
        self.viewVisitorsButton = QPushButton('View Visitors', self)
        self.viewShowsButton = QPushButton('View Shows', self)
        self.addShowButton = QPushButton('Add Show', self)
        self.viewStaff = QPushButton('View Staff', self)
        self.viewAnimals = QPushButton('View Animals', self)
        self.logOutButton = QPushButton('Log Out', self)

        #place buttons on the screen by column
        self.grid.addWidget(self.viewVisitorsButton, 0, 0)
        self.grid.addWidget(self.viewShowsButton, 1, 0)
        self.grid.addWidget(self.addShowButton, 2, 0)

        self.grid.addWidget(QLabel('  '), 0, 1)
        self.grid.addWidget(QLabel('  '), 1, 1)
        self.grid.addWidget(QLabel('  '), 2, 1)

        self.grid.addWidget(self.viewStaff, 0, 2)
        self.grid.addWidget(self.viewAnimals, 1, 2)
        self.grid.addWidget(self.logOutButton, 2, 2)  

        #test
        self.logOutButton.clicked.connect(self.switchScreens)      

        self.setLayout(self.grid)

        self.title = 'Atlanta Zoo'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def switchScreens(self):
        self.close()
        self.loginScreen = LoginScreen()
        self.loginScreen.show()
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = AdministratorFunctionality()
    main.show()
    sys.exit(app.exec_())
