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




"""
================================================================================
ANÁLISIS COMPARATIVO Y JUSTIFICACIÓN: PROGRAMACIÓN MODULAR VS. P.O.O.
================================================================================

1. DESCRIPCIÓN DE LO IMPLEMENTADO EN EL EJERCICIO:
   En este ejercicio se desarrollaron dos soluciones para el cálculo de métricas
   estadísticas (promedio y desviación estándar muestral con N=10):
   
   - Enfoque Modular-Estructurado: Se implementaron funciones independientes 
     (promedio y desviacion) que reciben el arreglo de datos como parámetro
     explícito en cada llamada y procesan la información de manera secuencial.
     
   - Enfoque Orientado a Objetos: Se diseñó e implementó la clase 'Estadistica', 
     la cual centraliza el conjunto de datos como un atributo privado (__datos) 
     y provee métodos miembro (promedio() y desviacion()) que operan sobre su 
     propio estado interno sin requerir el paso reiterado de parámetros.

2. VENTAJAS DE UTILIZAR LA PROGRAMACIÓN ORIENTADA A OBJETOS (P.O.O.):

   a) Encapsulamiento y Protección del Estado:
      Al declarar el atributo '__datos' con visibilidad privada, se restringe el
      acceso directo desde el entorno global. Esto previene modificaciones 
      accidentales o alteraciones de la muestra durante la secuencia de cálculo,
      garantizando la consistencia e integridad matemática de los resultados.

   b) Alta Cohesión:
      La estructura de datos y las operaciones matemáticas asociadas coexisten
      dentro de una misma unidad lógica ('Estadistica'). A diferencia del paradigma
      estructurado (donde las variables y las funciones quedan dispersas en el 
      ámbito del script), la POO agrupa la responsabilidad en una sola entidad.

   c) Abstracción y Reusabilidad:
      La clase opera bajo el principio de "caja negra". El programa principal solo 
      necesita instanciar el objeto e invocar los métodos requeridos, abstrayéndose 
      de las fórmulas internas (sumatorias, diferencias al cuadrado y raíz).
      Esto facilita su exportación e integración directa en otros módulos.

   d) Mantenibilidad y Extensibilidad:
      Si en el futuro se requiere calcular nuevas métricas (como varianza, mediana 
      o moda), estas se pueden añadir como nuevos métodos de la clase sin afectar 
      ni romper la lógica del código cliente existente.
================================================================================
"""