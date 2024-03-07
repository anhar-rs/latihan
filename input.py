import sys
from PyQt5 import QtWidgets, QtCore
import random

class MyWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setFixedSize(450, 500)
        self.setWindowTitle("Tugas 3 ANHAR")

        self.label = QtWidgets.QLabel(self)
        self.label.setText('x: 0, y: 0')
        self.label.setStyleSheet('color: black; font-size: 20px;')
        self.label.setGeometry(QtCore.QRect(0, 0, 150, 100))
        self.label.installEventFilter(self)  # Memasang event filter ke label

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.close()
        elif event.key() == QtCore.Qt.Key_R:
            self.moveLabelRandom()

    def moveLabelRandom(self):
        newX = random.randint(0, self.width() - self.label.width())
        newY = random.randint(0, self.height() - self.label.height())
        self.updateLabelPosition(newX, newY)

    def updateLabelPosition(self, x, y):
        self.label.setText(f'x: {x}, y: {y}')
        self.label.move(x, y)

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == QtCore.QEvent.Enter:
            self.moveLabelRandom()
            return True
        return super(MyWindow, self).eventFilter(obj, event)

    def mouseMoveEvent(self, event):
        self.updateLabelPosition(event.x(), event.y())

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(application.exec_())
