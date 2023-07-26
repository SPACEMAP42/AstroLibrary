import math
from astrolibrary.utils.geometry.RelOperator import *


class Point3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z

    def __str__(self) -> str:
        return "x:" + str(self._x) + ", y:" + str(self._y) + ", z:" + str(self._z)

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def z(self) -> float:
        return self._z

    def norm(self) -> float:
        return math.sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def unitVector(self):
        return Point3D(
            self._x / self.norm(),
            self._y / self.norm(),
            self._z / self.norm(),
        )

    def normalize(self):
        norm = self.norm()
        self._x = self._x / norm
        self._y = self._y / norm
        self._z = self._z / norm

    def set_point(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z

    def equal(self, point) -> bool:
        if EQ(self._x, point._x) and EQ(self._y, point._y) and EQ(self._z, point._z):
            return True
        else:
            return False

    def distance(self, point) -> float:
        diffX = self._x - point._x
        diffY = self._y - point._y
        diffZ = self._z - point._z
        return math.sqrt(diffX * diffX + diffY * diffY + diffZ * diffZ)

    def __sub__(self, point):
        diffX = self._x - point._x
        diffY = self._y - point._y
        diffZ = self._z - point._z
        return Point3D(diffX, diffY, diffZ)

    def __rsub__(self, point):
        return self.__sub__(point)

    def __add__(self, point):
        addX = self._x + point._x
        addY = self._y + point._y
        addZ = self._z + point._z
        return Point3D(addX, addY, addZ)

    def __radd__(self, point):
        return self.__add__(point)

    def __mul__(self, other):
        result = Point3D(0.0, 0.0, 0.0)
        if isinstance(other, (int, float)):
            result.set_point(self._x * other, self._y * other, self._z * other)
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        result = Point3D(0.0, 0.0, 0.0)
        if isinstance(other, (int, float)):
            result.set_point(self._x / other, self._y / other, self._z / other)
        return result

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def dot_product(self, point) -> float:
        return self._x * point._x + self._y * point._y + self._z * point._z

    def cross_product(self, point):
        result = Point3D(
            self._y * point._z - self._z * point._y,
            self._z * point._x - self._x * point._z,
            self._x * point._y - self._y * point._x,
        )
        return result
