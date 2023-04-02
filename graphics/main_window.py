from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, init_pos, size, title):
        super().__init__()
        self.pos = init_pos
        self.size = size
        self.setWindowTitle(title)
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.setGeometry(*init_pos, *size)
        self.initTimer()
        self.children=[]
        self.show()
    
    def initTimer(self):
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update)
        self._timer.start(100000 // 60) # 60 FPS
    
    def addChild(self, child):
        self.children.append(child)
        
    def _update(self):
        for child in self.children:
            child._update()
