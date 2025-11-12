def suma(a, b):
    return round(a + b,2)
def resta(a, b):
    return round(a - b,2)
def multiplicacion(a, b):
    return round(a * b,2)
def division(a, b):
    if b != 0:
        return round(a / b, 2)
    else:
        return "Error: División por cero"