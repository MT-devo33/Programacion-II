import math
from multimethod import multimethod

class Vector3D:

    @multimethod
    def __init__(self):
        self.__x = 0.0
        self.__y = 0.0
        self.__z = 0.0

    @multimethod
    def __init__(self, x: float, y: float, z: float):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def __add__(self, b: object):
        return Vector3D(self.__x + b.getX(), self.__y + b.getY(), self.__z + b.getZ())

    def __mul__(self, r: float):
        return Vector3D(self.__x * r, self.__y * r, self.__z * r)

    def __rmul__(self, r: float):
        return Vector3D(self.__x * r, self.__y * r, self.__z * r)

    def __abs__(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def normal(self):
        longitud = abs(self)
        if longitud == 0:
            return Vector3D(0.0, 0.0, 0.0)
        return Vector3D(self.__x / longitud, self.__y / longitud, self.__z / longitud)

    def __matmul__(self, b: object):
        return self.__x * b.getX() + self.__y * b.getY() + self.__z * b.getZ()

    def __xor__(self, b: object):
        rx = self.__y * b.getZ() - self.__z * b.getY()
        ry = self.__z * b.getX() - self.__x * b.getZ()
        rz = self.__x * b.getY() - self.__y * b.getX()
        return Vector3D(rx, ry, rz)

    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"


class Main():
    a = Vector3D(1.0, 2.0, 3.0)
    b = Vector3D(4.0, 5.0, 6.0)
    r = 2.5

    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print(f"Escalar r: {r}")

    c = a + b
    print(f"\na) Suma (a + b): {c}")

    mult1 = a * r
    mult2 = r * a
    print(f"b) Escalar (a * r): {mult1}")
    print(f"b) Escalar (r * a): {mult2}")

    print(f"c) Longitud (|a|): {abs(a):.4f}")

    print(f"d) Normal de a: {a.normal()}")

    pe = a @ b
    print(f"e) Producto escalar (a @ b): {pe:.2f}")

    pv = a ^ b
    print(f"f) Producto vectorial (a ^ b): {pv}")