#BlackJack
import random
import time
print("Bienvenido al Black Jack")
time.sleep(2)
ronda = 1
puntuacion_jugador = 0
puntuacion_banca = 0
opciones = ["pedir","plantar"]

print("Turno de la banca: ")
for i in range(3):
    tirada_banca = random.randint(1,6)
    puntuacion_banca += tirada_banca
    print("A la banca le ha tocado un",tirada_banca)

time.sleep(4)

print("Tu turno: ")
for i in range(3):
    tirada_jugador = random.randint(1,6)
    puntuacion_jugador += tirada_jugador
    print("Te ha tocado un",tirada_jugador)
time.sleep(4)

print("\n*******************************")
print("Tienes un",puntuacion_jugador)
print("La banca tiene un",puntuacion_banca)
print("*******************************\n")


jugando = True
while jugando:
    pide_carta = input("Quieres plantarte(p) o pedir carta(c)?(p/c): ")

    if pide_carta == "c":
        tirada_jugador = random.randint(1,6)
        puntuacion_jugador += tirada_jugador
        print("Te ha tocado un",tirada_jugador)
        print("Tienes",puntuacion_jugador,"puntos")
        if puntuacion_jugador > 21:
            print("Te has pasado de 21")
            jugando = False

    elif pide_carta == "p":
        print("Tienes",puntuacion_jugador,"puntos")
        jugando = False

    else:
        print("Respuesta incorrecta")

time.sleep(2)
turno_banca = True        
while turno_banca:
    print("\nTurno de la banca:")
    time.sleep(2)
    if puntuacion_banca > 15:
        print("La banca se planta")
        turno_banca = False
    else:
        tirada_banca = random.randint(1,6)
        puntuacion_banca += tirada_banca
        print("A la banca le ha tocado un",tirada_banca)
        print("Tiene",puntuacion_banca,"puntos")
print("\nY el resultado final es...............")   
time.sleep(2)  
if puntuacion_jugador > 21:
    print("Te has pasado, has perdido.")
elif puntuacion_banca > 21:
    print("La banca se ha pasado, has ganado!")
elif puntuacion_jugador > puntuacion_banca:
    print("Has ganado!!")
elif puntuacion_banca == puntuacion_jugador:
    print("Habeis quedado empate!")
else:
    print("Has perdido!")

print("\n*******************************")
print("Tenias un",puntuacion_jugador)
print("La banca tenia un",puntuacion_banca)
print("*******************************")