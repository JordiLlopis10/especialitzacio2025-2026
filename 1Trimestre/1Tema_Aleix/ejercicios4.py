#4.1
"""
num = 1
while num <= 10:
    print("Numero:", num)
    num += 1
"""

#4.2
"""
num = 10
while num >= 0:
    print("Numero:", num)
    num -= 1
print("Despegue!")
"""

#4.3
"""
num = int(input("dime una contraseña: "))
contra = 1234

while num != contra:
    print("Contraseña incorrecta!")
    num = int(input("dime una contraseña: "))
print("Contraseña correcta!")
"""

#4.4
""""
contador = 0
mayor = 0
menor = 0
while contador < 10:
    nota = int(input("Dime una nota: "))
    if nota >= 5:
        mayor += 1
    else:
        menor += 1
    contador += 1
print("Hay",mayor,"notas mayores o iguales a 5 y",menor,"notas menores")
"""

#4.5
"""
num = 2
suma = 0
while num != 0:
    num = int(input("Dime un numero: "))
    suma = suma + num
print("La suma es:",suma)
"""