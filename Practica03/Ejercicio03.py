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
    vehiculo = VehiculoAutonomo("VH-001", "4K", 150)

    print("--- DATOS DEL VEHICULO AUTONOMO ---")
    print(f"Tipo: {vehiculo.tipo}")
    print(f"ID: {vehiculo.getId()}")
    print(f"Resolucion: {vehiculo.getResolucion()}")
    print(f"Alcance: {vehiculo.getAlcance()} metros")
    print(f"Estado encendido inicial: {vehiculo.getEncendido()}")

    print("\n--- PRUEBA DE METODOS ---")
    vehiculo.activar()
    print(f"Estado encendido actual: {vehiculo.getEncendido()}")
    vehiculo.desactivar()
    print(f"Estado encendido actual: {vehiculo.getEncendido()}")