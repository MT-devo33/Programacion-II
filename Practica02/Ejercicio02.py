import math

class AlgebraVectorial:
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

    def modulo(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def sumar(self, b):
        return AlgebraVectorial(self.__x + b.getX(), self.__y + b.getY(), self.__z + b.getZ())

    def restar(self, b):
        return AlgebraVectorial(self.__x - b.getX(), self.__y - b.getY(), self.__z - b.getZ())

    def productoEscalar(self, b):
        return self.__x * b.getX() + self.__y * b.getY() + self.__z * b.getZ()

    def productoVectorial(self, b):
        rx = self.__y * b.getZ() - self.__z * b.getY()
        ry = self.__z * b.getX() - self.__x * b.getZ()
        rz = self.__x * b.getY() - self.__y * b.getX()
        return AlgebraVectorial(rx, ry, rz)

    def perpendicular(self, b, metodo=0):
        if metodo == 1:
            return abs(self.sumar(b).modulo() - self.restar(b).modulo()) < 1e-9
        elif metodo == 2:
            mod_suma_cuad = self.sumar(b).modulo() ** 2
            suma_cuads = (self.modulo() ** 2) + (b.modulo() ** 2)
            return abs(mod_suma_cuad - suma_cuads) < 1e-9
        return abs(self.productoEscalar(b)) < 1e-9

    def paralela(self, b, r=None):
        if r is not None:
            cx = abs(self.__x - r * b.getX()) < 1e-9
            cy = abs(self.__y - r * b.getY()) < 1e-9
            cz = abs(self.__z - r * b.getZ()) < 1e-9
            return cx and cy and cz
        return self.productoVectorial(b).modulo() < 1e-9

    def proyeccion(self, b):
        escalar = self.productoEscalar(b) / (b.modulo() ** 2)
        return AlgebraVectorial(escalar * b.getX(), escalar * b.getY(), escalar * b.getZ())

    def componente(self, b):
        return self.productoEscalar(b) / b.modulo()

    def __str__(self):
        return f"({self.__x:.2f}, {self.__y:.2f}, {self.__z:.2f})"


class Main():
    a = AlgebraVectorial(1.0, 0.0, 0.0)
    b = AlgebraVectorial(0.0, 2.0, 0.0)
    c = AlgebraVectorial(2.0, 0.0, 0.0)

    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print(f"Vector c: {c}")

    print("\n--- PERPENDICULARIDAD ---")
    print(f"a perpendicular a b (producto escalar): {a.perpendicular(b)}")
    print(f"a perpendicular a b (|a+b| == |a-b|): {a.perpendicular(b, 1)}")
    print(f"a perpendicular a b (Pitagoras): {a.perpendicular(b, 2)}")

    print("\n--- PARALELISMO ---")
    print(f"a paralelo a c (producto cruz): {a.paralela(c)}")
    print(f"c paralelo a a con r=2.0: {c.paralela(a, 2.0)}")

    v1 = AlgebraVectorial(3.0, 4.0, 0.0)
    v2 = AlgebraVectorial(2.0, 0.0, 0.0)
    print("\n--- PROYECCION Y COMPONENTE ---")
    print(f"Proyeccion de v1 sobre v2: {v1.proyeccion(v2)}")
    print(f"Componente de v1 en v2: {v1.componente(v2):.2f}")