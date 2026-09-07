import math

class MiPunto:
    # b) y c) 
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    # a) 
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # d) y e)
    def distancia(self, punto_o_x, y=None):
        if isinstance(punto_o_x, MiPunto):
            dx = self.__x - punto_o_x.getX()
            dy = self.__y - punto_o_x.getY()
        else:
            dx = self.__x - punto_o_x
            dy = self.__y - y
        return math.sqrt(dx ** 2 + dy ** 2)


class Main():
    p1 = MiPunto()
    p2 = MiPunto(10.0, 30.5)

    print(f"Punto 1: ({p1.getX()}, {p1.getY()})")
    print(f"Punto 2: ({p2.getX()}, {p2.getY()})")

    d1 = p1.distancia(p2)
    print(f"Distancia p1 a p2 (usando objeto): {d1:.4f}")

    d2 = p1.distancia(10.0, 30.5)
    print(f"Distancia p1 a (10, 30.5) (usando coordenadas): {d2:.4f}")