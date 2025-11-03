#1
"""
contador = 0
num = int(input("Dime un numero: "))
while num % 2 == 0:
    num = int(input("Dime un numero: "))
    contador += 1
else:
    print(contador)
"""

#2
"""
nota = int(input("Dime una nota: "))
while nota not in range(0,11):
    nota = int(input("Dime una nota"))
"""

#3
"""
contador = 5
while contador != 0:
    print(contador)
    contador -= 1
"""

#4
"""
numero = int(input("Dime un numero: "))
if numero < 0:
    print("Numero negativo")
else:
    while numero != 0:
        print(numero)
        numero -= 1
"""

#5
"""
num1 = int(input("Dime un numero: "))
num2 = int(input("Dime un numero mayor que el anterior: "))
if num1 > num2:
    print("Numero incorrecto")
else:

    while num1<=num2:
        print(num1)
        num1 += 1
"""

#6
"""
num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))
if num1 > num2:
    while num1 >= num2:
        print(num2)
        num2 += 1
elif num1 == num2:
    print("Son iguales")
else:
    while num1 <= num2:
        print(num1)
        num1 += 1
"""