from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.top = 150
        self.left = 150
        self.width = 1100
        self.height = 700
        self.title = 'Pac-man AI'
