#Piedra,papel,tijera v2
#Jordi Llopis Godino
#10/11/2025
#Descripcion: Juego piedra, papel, tijera añadiendo lagarto y spock

import random
from funciones import *

elecciones ={
    1:("piedra",(3,4)),
    2:("papel",(1,5)),
    3:("tijeras",(2,4)),
    4:("lagarto",(2,5)),
    5:("spock",(1,3))
}
#Creamos las listas para los historiales, creamos la variables de victorias tanto para el usuario como para la maquina y creamos la variable ronda para tener el conteo de las rondas
historial_usuario = []
historial_maquina = []
historial = []
victorias_usuario = 0
victorias_maquina = 0
ronda = 1

#preguntamos al usuario su nombre
nombre_usuario = input("Bienvenido al minijuego, cual es tu nombre? ")
rondas_correctas = True

#comprovamos que nos digan una ronda mayor a 1 y que sea impar
while rondas_correctas:
    rondas = int(input("Cuantas rondas quieres jugar {}?: ".format(nombre_usuario)))
    if rondas % 2 == 0:
        print("El numero de rondas debe ser impar")
    elif rondas <= 1:
        print("El numero de rondas debe ser mayor que 1")
    else:
        rondas_correctas = False
        print("Perfecto, vamos a jugar",rondas,"rondas")

#para terminar el bucle del juego el usuario o la maquina deberan tener mas victorias que la mitat de numero de rondas, si se juega a 5 rondas con tener 3 victorias ya ganas
while rondas // 2 >= victorias_usuario and rondas // 2 >= victorias_maquina:
    print("\nRonda {}".format(ronda))
        
    tirada_jugador = int(input("Que eliges,piedra(1), papel(2), tijeras(3), lagarto(4) o spock(5)?: "))

    #El jugador debera elegir una opcion valida que va del numero 1 al 5, cualquier otro numero sera incorrecto y nos volvera a pedir el numero
    while tirada_jugador not in [1,2,3,4,5]:
        print("Eleccion incorrecta, vuelve a intentarlo")
        tirada_jugador = int(input("\nQue elegies,piedra(1), papel(2), tijeras(3), lagarto(4) o spock(5)?: "))

    #Con el modulo random elegimos un numero del 1 al 5 para la maquina
    tirada_maquina = random.randint(1,5)
    print("La maquina ha elegido",elecciones[tirada_maquina][0])

    #Asignamos los numeros donde si la maquina tiene alguno de los dos numeros ganaremos la ronda
    gana_contra = elecciones[tirada_jugador][1]

    #Creamos la variable eleccion_jugador para tener el nombre de la eleccion que ha hecho el jugador y la maquina en la tirada, asi poder añadirlo en los historiales
    eleccion_jugador = elecciones[tirada_jugador][0]
    eleccion_maquina = elecciones[tirada_maquina][0]

    #Añadimos las variables anteriores en los historiales del usuario y de la maquina
    historial_usuario.append(eleccion_jugador)
    historial_maquina.append(eleccion_maquina)

    #Si el usuario y la maquina tienen el mismo numero es empate y no hay que hacer ninguna comprovacion mas
    if tirada_jugador == tirada_maquina:
        print( "empate" )

    #Si la maquina tiene un numero con los que ganariamos la ronda le damos la victoria al usuario.
    # Solo sumamos una ronda si gana el usuario o la maquina, si hay empate no, ya que debe haber un ganador de la ronda
    elif tirada_maquina in gana_contra:
        ronda += 1
        victorias_usuario += 1
        historial.append([ronda,eleccion_jugador,eleccion_maquina,nombre_usuario])
        print("Gana {}".format(nombre_usuario))
    #Ya solo que la opcion de que la maquina a ganado la ronda 
    else:
        ronda += 1
        victorias_maquina += 1
        historial.append([ronda,eleccion_jugador,eleccion_maquina,"Maquina"])
        print("Gana la maquina") 
    print("\nLlevas {} victorias, la maquina lleva {} victorias".format(victorias_usuario,victorias_maquina))
    

#Juego terminado, mostramos victorias, historiales personales y el historial global
print("\n************RESULTADOS FINALES************")
print("{} ha ganado {} rondas".format(nombre_usuario,victorias_usuario))
print("La maquina ha ganado {} rondas".format(victorias_maquina))
print("\nHistorial de {}: {}".format(nombre_usuario,historial_usuario))
print("Historial de la maquina: {}".format(historial_maquina))
print("\nHistorial general:", historial)
print("******************************************\n")