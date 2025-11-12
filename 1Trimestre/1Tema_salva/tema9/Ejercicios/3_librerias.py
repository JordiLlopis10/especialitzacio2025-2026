import math
import datetime
import os

#Calcular el area de un circulo
radio = float(input("Dime el radio del circulo: "))
area = math.pi * radio**2
print("El area del circulo es:",area)

#mostrar la fecha de nacimiento del alumno como objeto de fecha
anio = int(input("Dime el año de tu nacimiento: "))
mes = int(input("Dime el mes de tu nacimiento: "))
dia = int(input("Dime el dia de tu nacimiento: "))
fecha_nacimiento = datetime.date(anio,mes,dia)
print("Tu fecha de nacimiento es:",fecha_nacimiento)

#listar los archivos del directorio actual, fijate en que directorio estas trabajando
archivos = os.listdir('.')
print("Los archivos en el directorio actual son:")
for archivo in archivos:
    print(archivo)