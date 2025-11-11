#Piedra,papel,tijera v2
#Jordi Llopis Godino
#10/11/2025
#Descripcion: 

import random
from funciones import *
elecciones ={
    1:("piedra",(3,4)),
    2:("papel",(1,5)),
    3:("tijeras",(2,4)),
    4:("lagarto",(2,5)),
    5:("spock",(1,3))
}
historial_usuario = []
historial_maquina = []
historial = []
victorias_usuario = 0
victorias_maquina = 0
ronda = 1

nombre_usuario = input("Bienvenido al minijuego, cual es tu nombre? ")
rondas_correctas = True

while rondas_correctas:
    rondas = int(input("Cuantas rondas quieres jugar {}?: ".format(nombre_usuario)))
    if rondas % 2 == 0:
        print("El numero de rondas debe ser impar")
    elif rondas <= 1:
        print("El numero de rondas debe ser mayor que 1")
    else:
        rondas_correctas = False
        print("Perfecto, vamos a jugar",rondas,"rondas")

while rondas // 2 >= victorias_usuario and rondas // 2 >= victorias_maquina:
    print("\nRonda {}".format(ronda))
        
    tirada_jugador = int(input("Que eliges,piedra(1), papel(2), tijeras(3), lagarto(4) o spock(5)?: "))

    while tirada_jugador not in [1,2,3,4,5]:
        print("Eleccion incorrecta, vuelve a intentarlo")
        tirada_jugador = int(input("\nQue elegies,piedra(1), papel(2), tijeras(3), lagarto(4) o spock(5)?: "))

    tirada_maquina = random.randint(1,5)
    print("La maquina ha elegido",elecciones[tirada_maquina][0])
    gana_contra = elecciones[tirada_jugador][1]

    eleccion_jugador = elecciones[tirada_jugador][0]
    eleccion_maquina = elecciones[tirada_maquina][0]

    historial_usuario.append(eleccion_jugador)
    historial_maquina.append(eleccion_maquina)

    if tirada_jugador == tirada_maquina:
        print( "empate" )

    elif tirada_maquina in gana_contra:
        victorias_usuario += 1
        historial.append([ronda,eleccion_jugador,eleccion_maquina,nombre_usuario])

        print("Gana {}".format(nombre_usuario)) 
    else:
        victorias_maquina += 1
        historial.append([ronda,eleccion_jugador,eleccion_maquina,"Maquina"])
        print("Gana la maquina") 
    print("\nLlevas {} victorias, la maquina lleva {} victorias".format(victorias_usuario,victorias_maquina))
    ronda += 1


print("\n************RESULTADOS FINALES************")
print("{} ha ganado {} rondas".format(nombre_usuario,victorias_usuario))
print("La maquina ha ganado {} rondas".format(victorias_maquina))
print("\nHistorial de {}: {}".format(nombre_usuario,historial_usuario))
print("Historial de la maquina: {}".format(historial_maquina))
print("\nHistorial general:", historial)
print("******************************************\n")