#1
""""
num1 = float(input("Dime un numero: "))
num2 = float(input("Dime un numero: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"
print("La suma es:",suma,"la resta es:",resta,"el producto es:",producto,"la division es:",division)
"""

#2
"""
carnet = input("¿Tienes carnet? (s/n): ").lower()
coche = input("¿Tienes coche? (s/n): ").lower()

if carnet == "s" and coche == "s":
    print("Puedes conducir")
elif carnet == "s" or coche == "s":
    print("Tienes solo una de las condiciones necesarias, no puedes conducir solo")
else:
    print("No puedes conducir")

"""

#3

#def fahrenheit_celsius(fahrenheit):
"""
    Convierte una temperatura de grados Fahrenheit a grados Celsius.

    Parámetros
    fahrenheit : float
        Temperatura en grados Fahrenheit.

    Retorna
    float
        Temperatura equivalente en grados Celsius.
"""
#    celsius = (fahrenheit - 32) * 5/9
#    return celsius


#resultado = fahrenheit_celsius(200)
#print("200º Fahrenheit son:", round(resultado, 2), "ºC")

#4
"""
nombre = input("Como te llamas? ")
edad = int(input("Que edad tienes? "))
print("Buenos dias", nombre.upper())
if edad >= 18:
    print("Eres mayor de edad",edad)
else:
    print("No eres mayor de edad")
"""
#7
#print("Hola hoy es dia",23)

#10
x = 10
b = 10
print(x==b)