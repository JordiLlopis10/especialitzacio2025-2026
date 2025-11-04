#1
"""
def pedir_num():
    try:
        numero = input("Dime un numero: ")
        numero_entero = int(numero)
    except ValueError:
        print("El numero es invalido")
    else:
        print("Correcto, el numero es:",numero_entero)
    finally:
        print("Fin")
pedir_num()
"""

#2
"""
def dividir():
    try:
        numero1 = int(input("Dime un numero: "))
        numero2 = int(input("Dime otro numero: "))
        print(numero1//numero2)
    except ZeroDivisionError:
        print("No se peude dividir entre 0")
dividir()
"""

#3
"""
try:

    lista = [1,2,3,4,5]
    print(lista[5])
except IndexError:
    print("Posicion inexistente de la lista")
"""

#4
"""
try:
    nombre_archivo = input("Nombre del archivo: ")
    archivo = open(nombre_archivo,"r")
    contenido = archivo.read()
    print("Contenido del archivo:",contenido)
except FileNotFoundError:
    print("¡Error! El archivo no existe.")
finally:
    print("Programa finalizado.")
"""

#5
"""
def pedir_num():
    try:
        numero = input("Dime un numero: ")
        numero_entero = int(numero)
    except ValueError:
        print("El numero es invalido")
    else:
        print("Correcto, el numero es:",numero_entero)
    finally:
        print("Fin")
pedir_num()
"""

#6
"""
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print("Error, la edad es negativa")

else:
    print(f"Edad válida: {edad}")
    
"""

#7
"""
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    operacion = input("Introduce la operación (+, -, *, /): ")
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        resultado = num1 / num2
    else:
        raise ValueError("Operación no válida")
except ValueError as ve:
    print("Error de entrada:", ve)
except ZeroDivisionError as zde:
    print("Error de división:", zde)
else:
    print("El resultado de " + str(num1) + " " + operacion + " " + str(num2) + " es: " + str(resultado))
finally:
    print("Fin de la calculadora.")
"""


#8
def pedir_contraseña():
    try:
        contraseña = input("Introduce tu contraseña: ")
        if len(contraseña) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
    except ValueError as e:
        print("¡Error!", e)
    else:
        print("Contraseña válida.")

pedir_contraseña()

