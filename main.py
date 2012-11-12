#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from window import Window
from demoCanvas import DemoCanvas
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window(DemoCanvas)
    win.raise_()

    pts = [ 50.,   0.,  50.,
           -50.,   0.,  50.,
           -50.,   0., -50.,
            50.,   0., -50.,
            50.,  50., -50.,
           -50.,  50., -50.,
           -50.,  50.,  50.,
            50.,  50.,  50.,
            50.,   0., -50.,
           -50.,   0., -50.,
           -50.,  50., -50.,
            50.,  50., -50.,
           -50.,   0., -50.,
           -50.,   0.,  50.,
           -50.,  50.,  50.,
           -50.,  50., -50.,
           -50.,   0.,  50.,
            50.,   0.,  50.,
            50.,  50.,  50.,
           -50.,  50.,  50.,
            50.,   0.,  50.,
            50.,   0., -50.,
            50.,  50., -50.,
            50.,  50.,  50. ]

    inds = [0, 1, 2, 2, 3, 0, 4, 5, 6, 6, 7,
            4, 8, 9, 10, 10, 11, 8, 12, 13,
            14, 14, 15, 12, 16, 17, 18, 18,
            19, 16, 20, 21, 22, 22, 23, 20]

    import numpy
    pts = numpy.array(pts, 'f').reshape(-1, 3)
    inds = numpy.array(inds, 'uint16')

    win.canvas.updatePoints(pts)
    win.canvas.updateIndices(inds)

    retcode = app.exec_()
    sys.exit(retcode)

if __name__ == '__main__':
    main()
