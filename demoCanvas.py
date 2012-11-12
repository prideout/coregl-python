import math
import numpy as np

from OpenGL.GL import *
from shaders import *
from utility import *
from canvas import *

class DemoCanvas(Canvas):
    def __init__(self, parent):
        super(DemoCanvas, self).__init__(parent)
        self.setMinimumSize(500, 500)
        self.indexCount = 0

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if not self.indexCount:
            return

        theta = time() * math.pi * 2
        eye = V3(20 * math.sin(theta), 100, 200)
        target = V3(0, 0, 0)
        up = V3(0, 1, 0)
        objToEye = look_at(eye, target, up)
        eyeToClip = perspective(45, self.aspect, 20, 600)
        normalM = np.resize(objToEye,(3,3))

        glUseProgram(self.programs['BareBones'])
        glUniformMatrix4fv(U("Projection"), 1, True, eyeToClip)
        glUniformMatrix4fv(U("Modelview"), 1, True, objToEye)
        glUniformMatrix3fv(U("NormalMatrix"), 1, True, normalM)
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.indexCount, GL_UNSIGNED_SHORT, None)

    def resizeGL(self, w, h):
        self.aspect = float(w) / float(h)
        glViewport(0, 0, w, h)

    def initializeGL(self):
        print glGetString(GL_VERSION)
        glClearColor(0.0, 0.25, 0.5, 1.0)
        self.programs = load_shaders()
        self.vao = glGenVertexArrays(1)
        self.pointsVbo = glGenBuffers(1)
        self.indicesVbo = glGenBuffers(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indicesVbo)
        glBindBuffer(GL_ARRAY_BUFFER, self.pointsVbo)
        glVertexAttribPointer(Attribs.POSITION, 3, GL_FLOAT, GL_FALSE, 12, None)
        glEnableVertexAttribArray(Attribs.POSITION)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

    def updatePoints(self, points):
        glBindBuffer(GL_ARRAY_BUFFER, self.pointsVbo)
        glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)

    def updateIndices(self, indices):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indicesVbo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)
        self.indexCount = len(indices)
