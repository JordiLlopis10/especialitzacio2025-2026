#!/usr/bin/env python

"""Script que muestra la clasificación ida de la liga leyendo los
resultados de los partidos del archivo liga.csv"""

import csv
import os

ARCHIVO = "liga.csv"


def leer_partidos():
    """Función que lee el fichero CSV y devuelve los datos del mismo en una
	lista de diccionarios con los datos de la liga."""
    with open(ARCHIVO, 'r', encoding='utf-8') as fichero:
        contenido = csv.DictReader(fichero)
        return list(contenido)


def equipos(liga):
    """Función que recibe la lista de diccionarios con los datos de la liga
    y devuelve un conjunto con los equipos de la liga."""
    conjunto = set()

    for partido in liga:
        conjunto.add(partido["Team 1"])
        conjunto.add(partido["Team 2"])

    return conjunto


def quien_gana(resultado):
    """Función que recibe un resultado y devuelve un 0 si es un empate,
	un 1 si gana el equipo de casa y -1 si gana el equipo visitante."""
    g1, g2 = resultado.split("-")
    g1, g2 = int(g1), int(g2)

    if g1 > g2:
        return 1
    elif g1 < g2:
        return -1
    else:
        return 0


def puntos(info):
    """Función que recibe una lista con los partidos ganados,
	empatados y perdidos, y devuelve los puntos obtenidos."""
    ganados, empatados, perdidos = info
    return ganados * 3 + empatados


def info_equipos(liga, *lista_equipos):
    """Función que recibe la lista de diccionarios con los datos de la liga y
	el conjunto de equipos y devuelve una lista de tuplas, en cada tupla se 
	guarda un equipo con los partidos ganados, empatados y perdidos y los 
	puntos obtenidos."""
    lista_equipos = lista_equipos[0]  # es un conjunto

    estadisticas = {equipo: [0, 0, 0] for equipo in lista_equipos}

    for partido in liga:
        eq1 = partido["Team 1"]
        eq2 = partido["Team 2"]
        res = partido["FT"]

        resultado = quien_gana(res)

        if resultado == 1:
            estadisticas[eq1][0] += 1   # gana equipo 1
            estadisticas[eq2][2] += 1   # pierde equipo 2
        elif resultado == -1:
            estadisticas[eq2][0] += 1   # gana equipo 2
            estadisticas[eq1][2] += 1   # pierde equipo 1
        else:
            estadisticas[eq1][1] += 1   # empate
            estadisticas[eq2][1] += 1

    # Convertir a lista de tuplas completas
    salida = []
    for equipo, datos in estadisticas.items():
        g, e, p = datos
        salida.append((equipo, g, e, p, puntos((g, e, p))))

    return salida


def clasificacion(datos):
    """Recibe la lista generada con la función anterior y la ordena según
	el número de puntos."""
    return sorted(datos, key=lambda x: x[4], reverse=True)


def imp_clasificacion(liga):
    """recibe la lista de diccionarios con los generado a parir del fichero csv,
	genera los datos de la clasificación y los imprime por pantalla"""
    lista_equipos = equipos(liga)
    datos = info_equipos(liga, lista_equipos)
    tabla = clasificacion(datos)

    print(f"{'Equipo':<15} {'G':<5} {'E':<5} {'P':<5} {'Pts':<5}")
    print("-" * 40)

    for equipo, g, e, p, pt in tabla:
        print(f"{equipo:<15} {g:<5} {e:<5} {p:<5} {pt:<5}")


if __name__ == '__main__':
    liga = leer_partidos()
    imp_clasificacion(liga)
