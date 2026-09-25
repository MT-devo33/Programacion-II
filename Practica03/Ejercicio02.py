import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.__vidasIniciales = int(numeroDeVidas)
        self.__numeroDeVidas = int(numeroDeVidas)
        self.__record = 0

    def reiniciaPartida(self):
        self.__numeroDeVidas = self.__vidasIniciales

    def actualizaRecord(self):
        if self.__numeroDeVidas > self.__record:
            self.__record = self.__numeroDeVidas
            print(f"Nuevo record alcanzado: {self.__record} vidas restantes.")
        else:
            print(f"Record actual: {self.__record}")

    def quitaVida(self):
        self.__numeroDeVidas -= 1
        return self.__numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.__numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.__numeroAAdivinar = random.randint(0, 10)
        print("Adivine un numero entre el 0 y el 10.")

        while True:
            intento = int(input("Ingrese su intento: "))

            if not self.validaNumero(intento):
                continue

            if intento == self.__numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                le_quedan_vidas = self.quitaVida()
                if le_quedan_vidas:
                    if intento < self.__numeroAAdivinar:
                        print("El numero a adivinar es mayor.")
                    else:
                        print("El numero a adivinar es menor.")
                    print("Intente de nuevo.\n")
                else:
                    print("Ya no le quedan mas vidas al jugador. Fin del juego.")
                    break


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 == 0:
            return True
        print("Error: El numero debe ser par y estar entre el 0 y 10.")
        return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 != 0:
            return True
        print("Error: El numero debe ser impar y estar entre el 0 y 10.")
        return False


class Main():
    juego_normal = JuegoAdivinaNumero(3)
    juego_par = JuegoAdivinaPar(3)
    juego_impar = JuegoAdivinaImpar(3)

    print("--- 1. JUEGO ADIVINA NUMERO NORMAL ---")
    juego_normal.juega()

    print("\n--- 2. JUEGO ADIVINA NUMERO PAR ---")
    juego_par.juega()

    print("\n--- 3. JUEGO ADIVINA NUMERO IMPAR ---")
    juego_impar.juega()