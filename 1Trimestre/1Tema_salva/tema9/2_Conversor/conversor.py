#temperatura
def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


#Longitud


def metros_kilometro(metros):
    kilometro = metros / 1000
    return round(kilometro, 2)



def kilometro_metro(kilometro):
    metro = kilometro * 1000
    return round(metro, 2)


# --- Divisas ---
def euro_dolar(euro):
    dolar = euro * 1.16
    return round(dolar, 2)

def dolar_euro(dolar):
    euro = dolar * 0.86
    return round(euro, 2)
