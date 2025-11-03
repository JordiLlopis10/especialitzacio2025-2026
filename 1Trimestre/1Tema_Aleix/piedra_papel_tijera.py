import random

victorias_usuario = 0
victorias_ia = 0
opciones = ["piedra", "papel", "tijera"]

# Pedir número impar de rondas
while True:
    rondas = int(input("Dime cuántas rondas quieres jugar (mejor de N, impar): "))
    if rondas % 2 != 0:
        break
    print("¡El número debe ser impar!")

ronda = 1
max_victorias = rondas // 2 + 1

while victorias_usuario < max_victorias and victorias_ia < max_victorias:
    print("\nRonda " + str(ronda))
    eleccion_usuario = int(input("Piedra (0), Papel (1), Tijera (2): "))

    if eleccion_usuario not in [0, 1, 2]:
        print("Elección inválida. La IA gana esta ronda automáticamente.")
        victorias_ia += 1
        ronda += 1
        continue

    eleccion_ia = random.randint(0, 2)
    print("La IA eligió: " + opciones[eleccion_ia])

    if eleccion_usuario == eleccion_ia:
        print("¡Empate! Esta ronda no cuenta.")
        continue  # no se aumenta ronda
    elif (eleccion_usuario == 0 and eleccion_ia == 2) or \
         (eleccion_usuario == 1 and eleccion_ia == 0) or \
         (eleccion_usuario == 2 and eleccion_ia == 1):
        print("¡Ganaste esta ronda!")
        victorias_usuario += 1
    else:
        print("¡La IA gana esta ronda!")
        victorias_ia += 1

    ronda += 1

print("\n--- RESULTADO FINAL ---")
print("Victorias Usuario: " + str(victorias_usuario))
print("Victorias IA: " + str(victorias_ia))

if victorias_usuario > victorias_ia:
    print("¡Felicidades, ganaste el juego!")
else:
    print("La IA ganó el juego, mejor suerte la próxima.")
