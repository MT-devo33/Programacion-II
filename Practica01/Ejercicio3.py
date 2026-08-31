import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b ** 2 - 4 * self.__a * self.__c)

    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if (discriminante < 0 or self.__a == 0):
            return 0
        if discriminante == 0:
            return (-self.__b / (2 * self.__a))
        return (-self.__b + math.sqrt(discriminante)) / (2 * self.__a)

    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if (discriminante < 0 or self.__a == 0):
            return 0
        if discriminante == 0:
            return (-self.__b / (2 * self.__a))
        return (-self.__b - math.sqrt(discriminante)) / (2 * self.__a)



print("Ingrese a, b, c: ")
a, b, c = map(float, input().split())
E1 = EcuacionCuadratica(a, b, c)
discriminante = E1.getDiscriminante()

if discriminante > 0:
    r1 = E1.getRaiz1()
    r2 = E1.getRaiz2()
    print(f"las raices son: \n r1: {r1:.4f} \n r2: {r2:.4f}")

elif discriminante == 0:
    r = E1.getRaiz1()
    print(f"La ecuación tiene una raíz {r:.4f}")
else:
    print("La ecuación no tiene raíces reales")