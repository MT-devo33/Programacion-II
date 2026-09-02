####### USANDO POO ########################################################################################

import math

class Estadistica:
    """Clase para calcular métricas estadísticas de una muestra de datos."""

    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        """Obtiene el promedio de los valores."""
        if not self.__datos:
            return 0.0
        
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        """Devuelve la desviación estándar de la muestra."""
        n = len(self.__datos)
        if n <= 1:
            return 0.0
        
        prom = self.promedio()
        suma_diferencias_cuadrado = sum((x - prom) ** 2 for x in self.__datos)
        
        return math.sqrt(suma_diferencias_cuadrado / (n - 1))


print("-------------USANDO PROGRAMACION ORIENTADA A OBJETOS-------------")

while True:
    print("Ingrese 10 números separados por espacios (Ej: 1.9 2.5 3.7...):")
    entrada = input("> ")
    numeros = [float(x) for x in entrada.split()]

    if len(numeros) == 10:
        break
    elif len(numeros) < 10:
        print(f"Error: Ingresó solo {len(numeros)} números. Faltan {10 - len(numeros)}. Intente de nuevo.\n")
    else:
        print(f"Error: Ingresó {len(numeros)} números. Sobran {len(numeros) - 10}. Intente de nuevo.\n")

estadisticas = Estadistica(numeros)
print(f"El promedio es {estadisticas.promedio():.2f}")
print(f"La desviación estandard es {estadisticas.desviacion():.5f}\n")




############## USANDO PROGRAMACION MODULAR ESTRUCTURADA #######################################################

import math

def promedio(datos):
    if not datos:
        return 0.0
    return sum(datos) / len(datos)

def desviacion(datos):
    n = len(datos)
    if n <= 1:
        return 0.0
    prom = promedio(datos)
    suma_cuadrados = sum((x - prom) ** 2 for x in datos)
    return math.sqrt(suma_cuadrados / (n - 1))


print("------------USANDO PROGRAMACION MODULAR ESTRUCTURADA--------------")

while True:
    print("Ingrese 10 números separados por espacios (Ej: 1.9 2.5 3.7...):")
    entrada = input("> ")
    numeros = [float(x) for x in entrada.split()]

    if len(numeros) == 10:
        break
    elif len(numeros) < 10:
        print(f"Error: Ingresó solo {len(numeros)} números. Faltan {10 - len(numeros)}. Intente de nuevo.\n")
    else:
        print(f"Error: Ingresó {len(numeros)} números. Sobran {len(numeros) - 10}. Intente de nuevo.\n")

print(f"El promedio es {promedio(numeros):.2f}")
print(f"La desviación estandard es {desviacion(numeros):.5f}")



