import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygonF, QImage, QPixmap
from PyQt5.QtCore import Qt, QPointF

class GameWindow(QtWidgets.QWidget):

    def __init__(self, parent, init_pos, size, env):
        super().__init__(parent)
        self.pos = init_pos
        self.size = size
        self.setGeometry(*init_pos, *size)
        self.setObjectName('game_window')
        self.img_label = QtWidgets.QLabel(self)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.img_label)
        self.setLayout(self.layout)
        self.env = env
        self.show()
        
    def draw_border(self, painter, size):
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.NoBrush))
        painter.setRenderHint(QPainter.Antialiasing)
        points = [(0, 0), (size[0], 0), (size[0], size[1]), (0, size[1])]
        qpoints = [QPointF(point[0], point[1]) for point in points]
        polygon = QPolygonF(qpoints)
        painter.drawPolygon(polygon)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_border(painter, self.size)
        screen = self.env.getScreen()
        original_img = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format_RGB888)
        self.img_label.setGeometry(0, 0, *self.size)
        pixmap = QPixmap(original_img)
        pixmap = pixmap.scaled(*self.size, Qt.IgnoreAspectRatio)
        self.img_label.setPixmap(pixmap)
        painter.end()

    def _update(self):
        # Keys correspond with B, NULL, SELECT, START, U, D, L, R, A
        # index
        control_input = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0], np.int8)
        self.env.enterInput(control_input)
        self.update()
