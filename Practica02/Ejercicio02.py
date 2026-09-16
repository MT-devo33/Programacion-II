import math
from multimethod import multimethod

class AlgebraVectorial:

    # --- Sobrecarga de Constructores ---
    @multimethod
    def __init__(self):
        self.__x = 0.0
        self.__y = 0.0
        self.__z = 0.0

    @multimethod
    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = 0.0

    @multimethod
    def __init__(self, x: float, y: float, z: float):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    # --- Getters ---
    def getX(self): return self.__x
    def getY(self): return self.__y
    def getZ(self): return self.__z

    # --- Sobrecarga de Operadores Matemáticos ---
    def __add__(self, b):
        return AlgebraVectorial(self.__x + b.getX(), self.__y + b.getY(), self.__z + b.getZ())

    def __sub__(self, b):
        return AlgebraVectorial(self.__x - b.getX(), self.__y - b.getY(), self.__z - b.getZ())

    def __mul__(self, b):
        return (self.__x * b.getX()) + (self.__y * b.getY()) + (self.__z * b.getZ())

    def __abs__(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def cruz(self, b):
        cx = self.__y * b.getZ() - self.__z * b.getY()
        cy = self.__z * b.getX() - self.__x * b.getZ()
        cz = self.__x * b.getY() - self.__y * b.getX()
        return AlgebraVectorial(cx, cy, cz)

    def por_escalar(self, r):
        return AlgebraVectorial(self.__x * r, self.__y * r, self.__z * r)

    # --- Sobrecarga de Funciones con multimethod ---
    @multimethod
    def perpendicular(self, b: object):
        return round(self * b, 4) == 0

    @multimethod
    def perpendicular(self, b: object, metodo: int):
        if metodo == 1:
            return round(abs(self + b), 4) == round(abs(self - b), 4)
        elif metodo == 2:
            mod_suma_cuad = round(abs(self + b)**2, 4)
            suma_cuads = round(abs(self)**2 + abs(b)**2, 4)
            return mod_suma_cuad == suma_cuads
        return False

    @multimethod
    def paralela(self, b: object):
        return round(abs(self.cruz(b)), 4) == 0

    @multimethod
    def paralela(self, b: object, r: float):
        rb = b.por_escalar(r)
        return (round(self.__x, 4) == round(rb.getX(), 4) and 
                round(self.__y, 4) == round(rb.getY(), 4) and 
                round(self.__z, 4) == round(rb.getZ(), 4))

    def Proyeccion_de_a_sobre_b(self, b):
        escalar = (self * b) / (abs(b)**2)
        return b.por_escalar(escalar)

    def Componente_de_a_en_b(self, b):
        return (self * b) / abs(b)

    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"


# --- Ejecución Directa (Plantilla Fija) ---
class Main():
    a = AlgebraVectorial(2.0, 0.0, 0.0)
    b = AlgebraVectorial(0.0, 3.0)
    c = AlgebraVectorial(4.0, 0.0, 0.0)

    print(f"Vector A: {a}")
    print(f"Vector B: {b}")
    print(f"Vector C: {c}")
    print("-" * 35)

    print("--- PRUEBAS DE PERPENDICULARIDAD (A y B) ---")
    print(f"c) a . b = 0 -> {a.perpendicular(b)}")
    print(f"a) |a + b| = |a - b| -> {a.perpendicular(b, 1)}")
    print(f"d) |a + b|^2 = |a|^2 + |b|^2 -> {a.perpendicular(b, 2)}")

    print("\n--- PRUEBAS DE PARALELISMO (A y C) ---")
    print(f"f) a x c = 0 -> {a.paralela(c)}")
    print(f"e) a = rc (con r=0.5) -> {a.paralela(c, 0.5)}")

    print("\n--- PROYECCIÓN Y COMPONENTE (A sobre C) ---")
    print(f"g) Proyeccion de A sobre C: {a.Proyeccion_de_a_sobre_b(c)}")
    print(f"h) Componente de A en C: {a.Componente_de_a_en_b(c)}")