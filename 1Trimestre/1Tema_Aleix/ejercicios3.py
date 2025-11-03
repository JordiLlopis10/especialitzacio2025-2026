#3.1
""""
nota = int(input("Dime tu nota en POO: "))
if nota < 0 or nota > 10:
    print("nota incorrecta")
elif nota < 5:
    print("Insuficiente")
elif nota < 7:
    print("Suficiente")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
"""

#3.2
"""
num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))
if num1 > num2:
    print("El primer num es mayor")
elif num1 < num2:
    print("El segundo numero es mayor")
else:
    print("Son iguales")
"""

#3.3
"""
puntuacion1 = int(input("Dime la primera puntuacion: "))
puntuacion2 = int(input("Dime la segunda puntuacion: "))
puntuacion3 = int(input("Dime la tercera puntuacion: "))
mayor = puntuacion1

if puntuacion2 > mayor:
    mayor = puntuacion2
elif puntuacion3 > mayor:
    mayor = puntuacion3
print("La puntuacion mayor es",mayor)
"""

#3.4
"""
misones_totales = int(input("Dime cuantas misiones hay: "))
misones_completadas = int(input("Dime cuantas misiones has completado: "))
porcentaje = (misones_completadas / misones_totales) * 100
print(porcentaje)
if porcentaje < 50:
    print("Nivel no superado")
elif porcentaje < 75:
    print("Nivel superado *")
elif porcentaje < 90:
    print("Nivel superado **")
else:
    print("Nivel superado ***")
"""