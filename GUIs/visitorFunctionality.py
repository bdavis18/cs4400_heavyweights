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

class VisitorFunctionality(QWidget):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__()

        self.initVisitorFunctionality()

    def initVisitorFunctionality(self):

        self.grid = QGridLayout()

        self.searchExhibitButton = QPushButton('Search Exhibits', self)
        self.searchShowButton = QPushButton('Search Shows', self)
        self.searchAnimalButton = QPushButton('Search for Animals', self)
        self.viewExhibitHistory = QPushButton('View Exhibit History', self)
        self.viewShowHistory = QPushButton('View Show History', self)
        self.logOut = QPushButton('Log Out', self)

        self.grid.addWidget(self.searchExhibitButton, 0, 0)
        self.grid.addWidget(self.searchShowButton, 0, 2)
        self.grid.addWidget(self.searchAnimalButton, 1, 0)
        self.grid.addWidget(self.viewExhibitHistory, 1, 2)
        self.grid.addWidget(self.viewShowHistory, 2, 0)
        self.grid.addWidget(self.logOut, 2, 2)
        self.grid.addWidget(QLabel('  '), 0, 1)
        self.grid.addWidget(QLabel('  '), 1, 1)
        self.grid.addWidget(QLabel('  '), 2, 1)


        self.setLayout(self.grid)

        self.title = 'Atlanta Zoo'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = VisitorFunctionality()
    main.show()
    sys.exit(app.exec_())
