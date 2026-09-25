class Sensor:
    tipo = "Genérico"

    def __init__(self, id_sensor):
        self.__id = str(id_sensor)
        self.__encendido = False

    def getId(self):
        return self.__id

    def getEncendido(self):
        return self.__encendido

    def activar(self):
        self.__encendido = True
        print(f"[{self.tipo}] Sensor '{self.__id}' activado.")

    def desactivar(self):
        self.__encendido = False
        print(f"[{self.tipo}] Sensor '{self.__id}' desactivado.")


class Camara(Sensor):
    tipo = "Cámara"

    def __init__(self, id_sensor, resolucion):
        super().__init__(id_sensor)
        self.__resolucion = str(resolucion)

    def getResolucion(self):
        return self.__resolucion


class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"

    def __init__(self, id_sensor, alcance):
        super().__init__(id_sensor)
        self.__alcance = int(alcance)

    def getAlcance(self):
        return self.__alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"

    def __init__(self, id_vehiculo, resolucion, alcance):
        Sensor.__init__(self, id_vehiculo)
        self.__resolucion = str(resolucion)
        self.__alcance = int(alcance)

    def getResolucion(self):
        return self.__resolucion

    def getAlcance(self):
        return self.__alcance


class Main():
    vehiculo = VehiculoAutonomo("VH-001", "1080p", 200)

    print("--- ATRIBUTOS DE CLASE ---")
    print(f"Tipo: {vehiculo.tipo}")

    print("\n--- ATRIBUTOS DE INSTANCIA ---")
    print(f"ID: {vehiculo.getId()}")
    print(f"Resolucion: {vehiculo.getResolucion()}")
    print(f"Alcance: {vehiculo.getAlcance()} m")
    print(f"Estado inicial: {vehiculo.getEncendido()}")

    print("\n--- METODOS HEREDADOS ---")
    vehiculo.activar()
    print(f"Estado actual: {vehiculo.getEncendido()}")
    vehiculo.desactivar()
    print(f"Estado actual: {vehiculo.getEncendido()}")