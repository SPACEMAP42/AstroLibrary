from PySide6.QtOpenGLWidgets import QOpenGLWidget

import OpenGL

# OpenUSE_ACCELERATOR = False
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


import numpy as np


class CustomOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.localOrigin = np.array([0.0, 0.0, 0.0])
        self.localX = np.array([1.0, 0.0, 0.0])
        self.localY = np.array([0.0, 1.0, 0.0])
        self.localZ = np.array([0.0, 0.0, 1.0])
        self.zoomFactor = 1
        self.eyeDistance = 1000
        quadratic = gluNewQuadric()
        self.quadratic = quadratic

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

        gluQuadricNormals(self.quadratic, GLU_SMOOTH)

        glLineStipple(4, 0xAAAA)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.initialize_eye_position()
        self.zoom()
        print(f"zoom: {self.zoomFactor}")
        self.drawSphere()
        # draw()

    def zoom(self):
        glViewport(0, 0, self.width(), self.height())

        aspect_ratio = self.width() / self.height()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(45.0 / self.zoomFactor, aspect_ratio, 0.1, 10000.0)

        glMatrixMode(GL_MODELVIEW)
        return True

    def initialize_eye_position(self):
        target = self.localOrigin
        eyePt = self.localOrigin + self.localZ * self.eyeDistance
        print(target)
        print(eyePt)
        up = self.localY
        print(
            eyePt[0],
            eyePt[1],
            eyePt[2],
            target[0],
            target[1],
            target[2],
            up[0],
            up[1],
            up[2],
        )
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            eyePt[0],
            eyePt[1],
            eyePt[2],
            target[0],
            target[1],
            target[2],
            up[0],
            up[1],
            up[2],
        )

        return True

    def drawSphere(self, center=[0, 0, 0], radius=100, color=[0, 0, 0, 1]):
        glPushMatrix()
        glColor4f(color[0], color[1], color[2], color[3])
        glTranslated(center[0], center[1], center[2])
        gluSphere(self.quadratic, radius, 50, 50)
        glPopMatrix()

    def wheelEvent(self, event):
        print(f"factor:{self.zoomFactor}")
        print(f"event: {event}")
        print(f"delta: {event.angleDelta().y()}")
        self.zoomFactor += event.angleDelta().y() / 1000.0
        print(f"factor:{self.zoomFactor}")
        print(self.zoomFactor)
        if self.zoomFactor < 1:
            self.zoomFactor = 1
        event.accept()
