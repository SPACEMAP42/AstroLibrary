import math
import itertools
from typing import List
from datetime import datetime


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from astrolibrary.data.tle import TLE
from astrolibrary.data.constant import EARTH_RADIUS_KM


class VisualizationTool:
    def __init__(self):
        self.__tles = None
        self.__fig = plt.figure(figsize=(16, 8))
        self.__ax = self.__fig.add_subplot(111, projection="3d")
        self.__ax.set_xlabel("X Label")
        self.__ax.set_ylabel("Y Label")
        self.__ax.set_zlabel("Z Label")

    def draw_earth(self):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = EARTH_RADIUS_KM * np.outer(np.cos(u), np.sin(v))
        y = EARTH_RADIUS_KM * np.outer(np.sin(u), np.sin(v))
        z = EARTH_RADIUS_KM * np.outer(np.ones(np.size(u)), np.cos(v))
        self.__ax.plot_wireframe(x, y, z, color="b")

    def draw_tles_at_moment(self, tles: List[TLE], moment: datetime = datetime.now()):
        coordinates = [tle.position_vector_at_moment(moment) for tle in tles]
        xs, ys, zs = list(zip(*coordinates))
        # self.__ax.set_position([min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)])
        print(self.__find_distance_of_fartest_point(xs, ys, zs))
        self.__ax.scatter(xs, ys, zs, marker="o", s=3.0)

    def __find_distance_of_fartest_point(self, xs, ys, zs):
        def distance(x1, y1, z1, x2, y2, z2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

        max_distance = 0
        # max_point = None
        for point1 in list(zip(xs, ys, zs)):
            x1, y1, z1 = point1
            dist = distance(x1, y1, z1, 0, 0, 0)
            if dist > max_distance:
                max_distance = dist
                # max_point = (point1, point2)
        return max_distance

    def show(self):
        plt.show()
