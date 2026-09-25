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
        self._numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def generaAleatorio(self):
        return random.randint(0, 10)

    def juega(self):
        self.reiniciaPartida()
        self._numeroAAdivinar = self.generaAleatorio()
        print("Adivine un numero entre el 0 y el 10.")

        while True:
            intento = int(input("Ingrese su intento: "))

            if not self.validaNumero(intento):
                continue

            if intento == self._numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                le_quedan_vidas = self.quitaVida()
                if le_quedan_vidas:
                    if self._numeroAAdivinar > intento:
                        print("El numero a adivinar es mayor. Intente de nuevo.")
                    else:
                        print("El numero a adivinar es menor. Intente de nuevo.")
                else:
                    print("Ya no le quedan mas vidas al jugador.")
                    break


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def generaAleatorio(self):
        return random.choice([0, 2, 4, 6, 8, 10])

    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 == 0:
            return True
        print("Error: El numero debe ser PAR y estar entre 0 y 10.")
        return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def generaAleatorio(self):
        return random.choice([1, 3, 5, 7, 9])

    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 != 0:
            return True
        print("Error: El numero debe ser IMPAR y estar entre 0 y 10.")
        return False


class Aplicacion():
    def main():
        juego_normal = JuegoAdivinaNumero(3)
        juego_par = JuegoAdivinaPar(3)
        juego_impar = JuegoAdivinaImpar(3)

        print("--- INICIANDO JUEGO NORMAL ---")
        juego_normal.juega()

        print("\n--- INICIANDO JUEGO PAR ---")
        juego_par.juega()

        print("\n--- INICIANDO JUEGO IMPAR ---")
        juego_impar.juega()

    main()