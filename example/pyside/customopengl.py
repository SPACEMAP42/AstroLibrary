import time

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
import OpenGL

from astrolibrary.utils.geometry import TMatrix3D
from astrolibrary.utils.geometry import Point3D

# OpenUSE_ACCELERATOR = False
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


import numpy as np


class CustomOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.localOrigin = Point3D(0.0, 0.0, 0.0)
        self.localX = Point3D(1.0, 0.0, 0.0)
        self.localY = Point3D(0.0, 1.0, 0.0)
        self.localZ = Point3D(0.0, 0.0, 1.0)
        self.zoomFactor = 1
        self.eyeDistance = 1000
        quadratic = gluNewQuadric()
        self.quadratic = quadratic
        self.last_pos = None

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
        self.draw()

    def zoom(self):
        glViewport(0, 0, self.width(), self.height())

        aspect_ratio = self.width() / self.height()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if self.zoomFactor <= 0:
            self.zoomFactor = 0.01
        glOrtho(
            -15000 * aspect_ratio / self.zoomFactor,
            15000 * aspect_ratio / self.zoomFactor,
            -15000 / self.zoomFactor,
            15000 / self.zoomFactor,
            -15000,
            15000,
        )
        # gluPerspective(45.0 / self.zoomFactor, aspect_ratio, 0.01, 100000000.0)

        glMatrixMode(GL_MODELVIEW)
        return True

    def rotate_eye_position(self, angleX, angleY, angleZ):
        transformMat = TMatrix3D()
        transformMat.rotateArbitraryAxis(self.localX, angleX)
        transformMat.rotateArbitraryAxis(self.localY, angleY)
        transformMat.rotateArbitraryAxis(self.localZ, angleZ)

        self.localX = transformMat * self.localX
        self.localY = transformMat * self.localY
        self.localZ = transformMat * self.localZ

    def initialize_eye_position(self):
        target = self.localOrigin
        eyePt = self.localOrigin + self.localZ * self.eyeDistance
        up = self.localY
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            eyePt.x(),
            eyePt.y(),
            eyePt.z(),
            target.x(),
            target.y(),
            target.z(),
            up.x(),
            up.y(),
            up.z(),
        )

        return True

    def drawSphere(
        self, center=[0, 0, 0], radius=100, color=[0, 0, 0, 1], sphere_resolution=20
    ):
        glPushMatrix()
        glColor4f(color[0], color[1], color[2], color[3])
        glTranslated(center[0], center[1], center[2])
        gluSphere(self.quadratic, radius, sphere_resolution, sphere_resolution)
        glPopMatrix()

    def drawPoint(
        self,
        point=[0, 0, 200],
        color=[0, 0, 0, 1],
        point_size=3,
    ):
        # glDisable(GL_LIGHTING)
        glPointSize(point_size)
        glColor4f(color[0], color[1], color[2], color[3])
        glBegin(GL_POINTS)
        glVertex3f(point[0], point[1], point[2])
        glEnd()
        # glEnable(GL_LIGHTING)

    def drawPoints(self, points, color=[0, 0, 0, 1], point_size=3):
        start = time.time()  # 시작
        glPointSize(point_size)
        glColor4f(color[0], color[1], color[2], color[3])
        glDisable(GL_LIGHTING)
        glBegin(GL_POINTS)
        for point in points:
            glVertex3f(point[0][0], point[0][1], point[0][2])
        glEnd()
        glEnable(GL_LIGHTING)
        # print(f"draw: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력

    def wheelEvent(self, event):
        self.zoomFactor += event.angleDelta().y() / 1000.0

        # if self.zoomFactor < 1:
        #     self.zoomFactor = 0.001
        event.accept()
        self.update()

    def mousePressEvent(self, event):
        self.lastPos = event.pos()
        event.accept()
        self.update()

        # if event.modifiers() and Qt.ShiftModifier:
        #     gl_select(event.pos().x(), event.pos().y())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        angleScale = 0.001

        self.rotate_eye_position(angleScale * -dy, angleScale * -dx, 0.0)

        lastPos = event.pos()
        event.accept()
        self.update()

    def draw(self):
        pass
