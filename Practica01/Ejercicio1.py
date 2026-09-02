import time
import random

class Cronometro:
    """Clase Cronometro para medir intervalos de tiempo con alta precisión."""

    def __init__(self):
        self.__inicia = time.perf_counter()
        self.__finaliza = 0.0

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        """Restablece el tiempo de inicio a la hora actual."""
        self.__inicia = time.perf_counter()

    def detener(self):
        """Establece el tiempo final a la hora actual."""
        self.__finaliza = time.perf_counter()

    def lapso_de_tiempo(self):
        """Retorna el tiempo transcurrido en milisegundos."""
        return (self.__finaliza - self.__inicia) * 1000


def ordenacion_seleccion(lista):
    """Algoritmo de ordenación por selección."""
    n = len(lista)
    for i in range(n - 1):
        posicion_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[posicion_minimo]:
                posicion_minimo = j
        
        if i != posicion_minimo:
            lista[i], lista[posicion_minimo] = lista[posicion_minimo], lista[i]



tamano = 100000
numeros = [random.randint(0, 1000000) for _ in range(tamano)]

print(f"Iniciando ordenamiento por selección de {tamano} números...")


cronometro = Cronometro()
cronometro.inicia()

ordenacion_seleccion(numeros)

cronometro.detener()

print("Ordenamiento finalizado.")
print(f"Tiempo transcurrido: {cronometro.lapso_de_tiempo():.2f} milisegundos")

