class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__f = f
        self.__e = e

    def tieneSolucion(self):
        if self.__a * self.__d - self.__b * self.__c != 0:
            return True
        else:
            return False

    def getX(self):
        if self.tieneSolucion():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            print("no hay solucion...")
            return None

    def getY(self):
        if self.tieneSolucion():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        else:
            print("no hay solucion...")
            return None



a,b,c,d,e,f = map(float, input("ingrese a b c d e f: ").split())
E1 = EcuacionLineal(a,b,c,d,e,f)

print("Tiene solucion:")
if (E1.tieneSolucion() == True):
    print("SI TIENE SOLUCION!!!!")
else:
    print("NO TIENE SOLUCION...")

print("solucion de X:")
E1.getX()

print("solucion de Y:")
E1.getY()

