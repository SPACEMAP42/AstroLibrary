from customopengl import CustomOpenGL
from astrolibrary.data.constant import EARTH_RADIUS_KM


class AstroDisplay(CustomOpenGL):
    def __init__(self, parent=None):
        super().__init__()
        self.points = []

    def draw(self):
        # for point in self.points:
        self.drawPoints(self.points, color=[0, 1, 0, 1], point_size=2)
        self.drawSphere(radius=EARTH_RADIUS_KM, color=[0, 0, 1, 1])

    def clear_points(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)
