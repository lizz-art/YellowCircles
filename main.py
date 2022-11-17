from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.go)
        self.st = False
        self.show()

    def go(self):
        self.st = True
        self.update()

    def paintEvent(self, event):
        if self.st:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        # qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        qp.setBrush(QColor('yellow'))
        r = randint(1, 300)
        qp.drawEllipse(100, 100, r, r)
        self.st = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
