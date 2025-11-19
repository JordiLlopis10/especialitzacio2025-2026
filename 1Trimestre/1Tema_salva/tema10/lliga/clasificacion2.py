#!/usr/bin/env python

"""Script que muestra la clasificación ida de la liga leyendo los
resultados de los partidos del archivo liga.csv"""

import csv
import os

ARCHIVO = "liga.csv"


def leer_partidos():
	"""Función que lee el fichero CSV y devuelve los datos del mismo en una
	lista de diccionarios con los datos de la liga."""
	pass


def equipos(liga):
	"""Función que recibe la lista de diccionarios con los datos de la liga
	y devuelve un conjunto con los equipos de la liga."""
	pass

def quien_gana(resultado):
	"""Función que recibe un resultado y devuelve un 0 si es un empate,
	un 1 si gana el equipo de casa y -1 si gana el equipo visitante."""
	pass


def puntos(info):
	"""Función que recibe una lista con los partidos ganados,
	empatados y perdidos, y devuelve los puntos obtenidos."""
	pass


def info_equipos(liga, *equipos):
	"""Función que recibe la lista de diccionarios con los datos de la liga y
	el conjunto de equipos y devuelve una lista de tuplas, en cada tupla se 
	guarda un equipo con los partidos ganados, empatados y perdidos y los 
	puntos obtenidos."""
	pass


def clasificacion(datos):
	"""Recibe la lista generada con la función anterior y la ordena según
	el número de puntos."""
	pass


def imp_clasificacion(liga):
	"""recibe la lista de diccionarios con los generado a parir del fichero csv,
	genera los datos de la clasificación y los imprime por pantalla"""
	pass


if __name__ == '__main__':
	liga = leer_partidos()
	imp_clasificacion(liga)