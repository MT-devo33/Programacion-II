import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def __add__(self, otro):
        return Vector3D(self.__x + otro.getX(), self.__y + otro.getY(), self.__z + otro.getZ())

    def __mul__(self, escalar):
        return Vector3D(self.__x * escalar, self.__y * escalar, self.__z * escalar)

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __abs__(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def normal(self):
        longitud = abs(self)
        if longitud == 0:
            return Vector3D(0.0, 0.0, 0.0)
        return Vector3D(self.__x / longitud, self.__y / longitud, self.__z / longitud)

    def __matmul__(self, otro):
        return self.__x * otro.getX() + self.__y * otro.getY() + self.__z * otro.getZ()

    def __xor__(self, otro):
        rx = self.__y * otro.getZ() - self.__z * otro.getY()
        ry = self.__z * otro.getX() - self.__x * otro.getZ()
        rz = self.__x * otro.getY() - self.__y * otro.getX()
        return Vector3D(rx, ry, rz)

    def __str__(self):
        return f"({self.__x:.2f}, {self.__y:.2f}, {self.__z:.2f})"


class Main():
    a = Vector3D(1.0, 2.0, 3.0)
    b = Vector3D(4.0, 5.0, 6.0)
    r = 2.5

    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print(f"Escalar r: {r}")

    c = a + b
    print(f"Suma (a + b): {c}")

    mult1 = a * r
    mult2 = r * a
    print(f"Escalar (a * r): {mult1}")
    print(f"Escalar (r * a): {mult2}")

    print(f"Longitud (|a|): {abs(a):.4f}")

    print(f"Normal de a: {a.normal()}")

    pe = a @ b
    print(f"Producto escalar (a . b): {pe:.2f}")

    pv = a ^ b
    print(f"Producto vectorial (a x b): {pv}")