#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from window import *

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.raise_()

    #win.canvas.updatePoints(...)
    #win.canvas.updateIndices(...)

    retcode = app.exec_()
    sys.exit(retcode)

if __name__ == '__main__':
    main()
