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

    def juega(self):
        self.reiniciaPartida()
        self.__numeroAAdivinar = random.randint(0, 10)
        print("Adivine un numero entre el 0 y el 10.")

        while True:
            intento = int(input("Ingrese su intento: "))

            if intento == self.__numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                le_quedan_vidas = self.quitaVida()
                if le_quedan_vidas:
                    if self.__numeroAAdivinar > intento:
                        print("El numero a adivinar es mayor. Intente de nuevo.")
                    else:
                        print("El numero a adivinar es menor. Intente de nuevo.")
                else:
                    print("Ya no le quedan mas vidas al jugador.")
                    break


class Aplicacion():
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

    main()