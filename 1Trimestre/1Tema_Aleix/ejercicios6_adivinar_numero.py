import random

ronda = 1
intentos = int(input("Cuantos intentos quieres? "))
numero_secreto = random.randint(1,intentos*2)
lista_numeros = []
print(numero_secreto)

while ronda <= intentos:
    numero = int(input("Dime un número: "))

    while numero in lista_numeros or numero > intentos*2:
        if numero in lista_numeros:
            numero = int(input("Número ya intentado, dime otro: "))
        elif numero > intentos*2:
            numero = int(input("Número mayor al máximo permitido ({}), intenta otro: ".format(intentos*2)))

    lista_numeros.append(numero)

    if numero == numero_secreto:
        print("\n¡Has ganado crack!")
        break
    else:
        print("Ese no es el número, te quedan ",intentos - ronda," intentos")
        ronda += 1
else:
    print("Has perdido! El número era",numero_secreto)