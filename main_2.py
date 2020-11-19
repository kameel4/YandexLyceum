import sys, random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.paint)

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        x, y = random.randint(0, 200), random.randint(0, 200)
        x1, y1 = x, y
        qp.setBrush(QColor(250, 250, 0))
        qp.drawEllipse(x, y, x1, y1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
