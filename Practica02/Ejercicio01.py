import math
from multimethod import multimethod

class MiPunto:

    @multimethod
    def __init__(self):
        self.__x = 0.0
        self.__y = 0.0

    @multimethod
    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    @multimethod
    def distancia(self, otro: object):
        dx = self.__x - otro.getX()
        dy = self.__y - otro.getY()
        return math.sqrt(dx ** 2 + dy ** 2)

    @multimethod
    def distancia(self, x: float, y: float):
        dx = self.__x - x
        dy = self.__y - y
        return math.sqrt(dx ** 2 + dy ** 2)


class Main():
    p1 = MiPunto()
    p2 = MiPunto(10.0, 30.5)

    print(f"Punto 1: ({p1.getX()}, {p1.getY()})")
    print(f"Punto 2: ({p2.getX()}, {p2.getY()})")

    d1 = p1.distancia(p2)
    print(f"Distancia de p1 a p2: {d1:.4f}")

    d2 = p1.distancia(10.0, 30.5)
    print(f"Distancia de p1 a (10, 30.5): {d2:.4f}")