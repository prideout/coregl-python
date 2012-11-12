from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, canvasClass):
        super(Window, self).__init__()
        self.canvas = canvasClass(self)
        self.setCentralWidget(self.canvas)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('grasshopper')    
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
