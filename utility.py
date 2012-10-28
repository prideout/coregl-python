from PyQt4 import QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from time import time
import math

import numpy as np
from numpy import linalg as LA

# Set this 'None' to refresh as rapidly as possible
ThrottleFps = 60

# Provide a terse way to get a uniform location from its name
def U(name):
    p = glGetIntegerv(GL_CURRENT_PROGRAM)
    return glGetUniformLocation(p, name)

# Provide a terse way to create a f32 numpy 3-tuple
def V3(x, y, z):
    return np.array([x, y, z], 'f')

def translation(direction):
    M = np.identity(4)
    M[:3, 3] = direction[:3]
    return M

def look_at(eye, target, up):
    F = target[:3] - eye[:3]
    f = F / LA.norm(F)
    U = up / LA.norm(up)
    s = np.cross(f, U)
    u = np.cross(s, f)
    M = np.matrix(np.identity(4))
    M[:3,:3] = np.vstack([s,u,-f])
    T = translation(-eye)
    return np.matrix(M * T, 'f')

def perspective(fovy, aspect, f, n):
    s = 1.0/math.tan(math.radians(fovy)/2.0)
    sx, sy = s / aspect, s
    zz = (f+n)/(n-f)
    zw = 2*f*n/(n-f)
    m = np.matrix([[sx,0,0,0],
                   [0,sy,0,0],
                   [0,0,zz,zw],
                   [0,0,-1,0]], 'f')
    return m

class GLWidget(QGLWidget):
    def __init__(self, parent):
        if hasattr(QGLFormat, 'setVersion'):
            f = QGLFormat(); f.setVersion(3, 2)
            f.setProfile(QGLFormat.CoreProfile)
            c = QGLContext(f, None)
            QGLWidget.__init__(self, c, parent)
        else:
            QGLWidget.__init__(self, parent) 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateGL)
        interval = 1000.0 / ThrottleFps if ThrottleFps else 0
        self.timer.start( interval )
                        
    def paintGL(self):
        self.draw()

    def updateGL(self):
        self.draw()
        self.update()

    def draw(self):
        pass
