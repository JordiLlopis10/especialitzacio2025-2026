#1
"""
productos = ["Manzana","Platano","Pera","Banana","Uva"]
productos.append("Fresa")
productos.remove("Manzana")
print(productos)
"""


#2
"""
coordenadas = (125,603,10)
x,y,z = coordenadas
print(x,y,z)
"""

#3
"""
mates = {"Pepe","Carlos","Marcos","Maria"}
ingles = {"Carlos","Maria","Carla","Pedro"}

ambas = mates.intersection(ingles)
print(ambas)
"""

#4
"""
alumnos_notas = {"Pepe":5,"Marcos":7,"Maria":10,"Josep":1}
alumnos_notas["Jordi"] = 9
alumnos_notas["Josep"] = 6
for alumno,nota in alumnos_notas.items():
    print("Alumno {} - Nota : {}".format(alumno,nota))
"""

#5
"""
agenda = {"Pedro": 34543622,"Carles":23536,"Nando":6823151}

nuevo_nombre = input("Dime el nombre del contacto nuevo: ")
nuevo_numero = int(input("Dime su telefono: "))
agenda[nuevo_nombre] = nuevo_numero

buscar_nombre = input("Dime un nombre para buscar su numero: ")
print(agenda[buscar_nombre])

eliminar_contacto = input("Dime el nombre del contacto que quieras eliminar: ")
agenda.pop(eliminar_contacto)

print(agenda)
"""

#8
"""
numero = int(input("Dime un numero: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
"""
