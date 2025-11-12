"""Calculadora avanzada con operaciones básicas.

Este programa permite realizar operaciones de suma, resta,
multiplicación y división entre dos números ingresados por el usuario.
"""

def suma(a, b):
    """Devuelve la suma de dos números redondeada a dos decimales.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma redondeada a dos decimales.
    """
    return round(a + b, 2)


def resta(a, b):
    """Devuelve la resta de dos números redondeada a dos decimales.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la resta redondeada a dos decimales.
    """
    return round(a - b, 2)


def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números redondeada a dos decimales.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación redondeada a dos decimales.
    """
    return round(a * b, 2)


def division(a, b):
    """Devuelve la división de dos números redondeada a dos decimales.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float | str: Resultado de la división redondeada a dos decimales,
        o un mensaje de error si el divisor es cero.
    """
    if b != 0:
        return round(a / b, 2)
    return "Error: División por cero"


def main():
    """Función principal del programa."""
    print("Calculadora avanzada")
    print("Elige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Validar opción
    opcion = int(input("Elige una opción (1-4): "))
    #si el numero es menor que 1 o mayor que 4 entrara en el bucle
    while opcion < 1 or opcion > 4:
        opcion = int(input("Opción no válida, elige una opción (1-4): "))

    num1 = float(input("Dime el primer número: "))
    num2 = float(input("Dime el segundo número: "))

    if opcion == 1:
        resultado = suma(num1, num2)
    elif opcion == 2:
        resultado = resta(num1, num2)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
    else:
        resultado = division(num1, num2)

    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    main()
