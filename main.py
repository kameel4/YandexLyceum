import sys, random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 365)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "кнопка да"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupUi(self)
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
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, x1, y1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
