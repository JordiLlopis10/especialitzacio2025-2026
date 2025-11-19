import random


def pedir_rondas(nombre_usuario):
    rondas = int(input("Cuantas rondas quieres jugar {}?: ".format(nombre_usuario)))
    return rondas
    

def pedir_nombre():
    nombre_usuario = input("Bienvenido al minijuego, cual es tu nombre? ")
    return nombre_usuario


def tirada_usuario():
    tirada_jugador = int(input("Que eliges,piedra(1), papel(2), tijeras(3), lagarto(4) o spock(5)?: "))
    return tirada_jugador


def tirada_ia():
    tirada_maquina = random.randint(1,5)
    return tirada_maquina


# def determinar_ganador(maquina,gana_contra):
    

# def mostrar_resultado():

# def mostrar_historial():

# def anyadir_a_fichero():
