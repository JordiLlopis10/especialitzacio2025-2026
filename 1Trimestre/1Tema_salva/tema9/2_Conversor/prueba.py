from conversor import *
while True:
    print("-----------------------------------")
    print("Bienvenido al conversor de unidades")
    print("Elige una opcion:")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Convertir de Kilometros a Metros")
    print("4. Convertir de Metros a Kilometros")
    print("5. Convertir de Euros a Dolares")
    print("6. Convertir de Dolares a Euros")
    print("7. Salir")

    print("-----------------------------------")

    opcion = int(input("Elige una opcion (1-7): "))

    if opcion == 1:
        celsius = float(input("Introduce la temperatura en Celsius: "))
        print(f"{celsius} grados Celsius son {celsius_fahrenheit(celsius)} grados Fahrenheit")

    elif opcion == 2:
        fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
        print(f"{fahrenheit} grados Fahrenheit son {fahrenheit_celsius(fahrenheit)} grados Celsius")

    elif opcion == 3:
        kilometros = float(input("Introduce la distancia en Kilometros: "))
        print(f"{kilometros} kilometros son {kilometro_metro(kilometros)} metros")

    elif opcion == 4:
        metros = float(input("Introduce la distancia en Metros: "))
        print(f"{metros} metros son {metros_kilometro(metros)} kilometros")

    elif opcion == 5:
        euros = float(input("Introduce la cantidad en Euros: "))
        print(f"{euros} euros son {euro_dolar(euros)} dolares")

    elif opcion == 6:
        dolares = float(input("Introduce la cantidad en Dolares: "))
        print(f"{dolares} dolares son {dolar_euro(dolares)} euros")
    
    elif opcion == 7:
        print("Saliendo del conversor...")
        break
    else:
        print("Opcion no valida")
