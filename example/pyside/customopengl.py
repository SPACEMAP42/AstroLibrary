from PySide6.QtOpenGLWidgets import QOpenGLWidget

import OpenGL

# OpenUSE_ACCELERATOR = False
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


from OpenGLContext import testingcontext

BaseContext = testingcontext.getInteractive()

import numpy as np


class CustomOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.localOrigin = [0.0, 0.0, 0.0]
        self.localX = [1.0, 0.0, 0.0]
        self.localY = [0.0, 1.0, 0.0]
        self.localZ = [0.0, 0.0, 1.0]
        self.zoomFactor = 1
        self.eyeDistance = 1000

    def initializeGL(self):
        glClearColor(1, 1, 1, 0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glClearDepth(10000)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        glEnable(GL_CULL_FACE)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 10, 1.0])

        glEnable(GL_COLOR_MATERIAL)

        qObj = gluNewQuadric()
        gluQuadricNormals(qObj, GLU_SMOOTH)

        glLineStipple(STIPPLE_FACTOR, STIPPLE_PATTERN)

    def paintGL(self):
        glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        # self.initialize_eye_position()
        self.render_example_cube()
        # zoom(self.zoomFactor)
        # draw()

    def initialize_eye_position(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        target = self.localOrigin
        eyePt = self.localOrigin + self.localZ * 1000
        eyePt = self.localOrigin + self.localZ * self.eyeDistance
        up = self.localY

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            eyePt[0],
            eyePt[1],
            eyePt[1],
            target[0],
            target[1],
            target[2],
            up[0],
            up[1],
            up[2],
        )

        return True

    def render_example_cube(self):
        glColor3f(1.0, 1.0, 1.0)
        glLoadIdentity()  # clear the matrix
        # viewing transformation
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glScalef(1.0, 2.0, 1.0)  # modeling transformation
        glutWireCube(1.0)
        glFlush()
