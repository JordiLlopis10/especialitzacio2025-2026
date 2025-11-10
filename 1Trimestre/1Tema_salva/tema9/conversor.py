#temperatura
def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

def celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 2)

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)

def fahrenheit_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    return round(kelvin, 2)

def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

def kelvin_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return round(fahrenheit, 2)

#Longitud

def metros_centimetros(metros):
    centimetros = metros * 100
    return round(centimetros, 2)

def metros_kilometro(metros):
    kilometro = metros / 1000
    return round(kilometro, 2)

def centimetros_metro(centimetros):
    metro = centimetros / 100
    return round(metro, 2)

def centimetros_kilometro(centimetros):
    kilometro = centimetros / 100000
    return round(kilometro, 2)

def kilometro_metro(kilometro):
    metro = kilometro * 1000
    return round(metro, 2)

def kilometro_centimetro(kilometro):
    centimetro = kilometro * 100000
    return round(centimetro, 2)

# --- Divisas ---
def euro_dolar(euro):
    dolar = euro * 1.16
    return round(dolar, 2)

def euro_dirham(euro):
    dirham = euro * 10.71
    return round(dirham, 2)

def dolar_euro(dolar):
    euro = dolar * 0.86
    return round(euro, 2)

def dolar_dirham(dolar):
    dirham = dolar * 9.27
    return round(dirham, 2)

def dirham_euro(dirham):
    euro = dirham / 10.71
    return round(euro, 2)

def dirham_dolar(dirham):
    dolar = dirham / 9.27
    return round(dolar, 2)
