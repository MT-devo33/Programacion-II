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



print("Ingrese 10 números separados por espacios (Ej: 1.9 2.5 3.7...):")
entrada = input("> ")

numeros = [float(x) for x in entrada.split()]

if len(numeros) != 10:
    print("Error: Debe ingresar exactamente 10 números.")
else:
    estadisticas = Estadistica(numeros)
    
    print(f"El promedio es {estadisticas.promedio():.2f}")
    print(f"La desviación estandar es {estadisticas.desviacion():.5f}")