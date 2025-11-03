#1
"""
lado_rectangulo = 23
superficie = lado_rectangulo * lado_rectangulo
perimetro = lado_rectangulo * 4
print("Superficie:", superficie,"\nPerimetro:",perimetro)
"""

#2
""""
temperatura = 32
fahrenheit = (temperatura*9/5)+32
print(temperatura,"grados en Fahrenheit son:",fahrenheit)
"""

#3
"""
plaza_lado = 20
superficie_plaza = plaza_lado * plaza_lado

radio_fuente = 4
superficie_fuente = 3.1416 * radio_fuente ** 2

superficie_libre = superficie_plaza - superficie_fuente

print("Superficie plaza:", superficie_plaza)
print("Superficie fuente:", superficie_fuente)
print("Superficie libre:",superficie_libre)
"""

#4
"""
precio=int(input("Cuanto valia el producto? "))
numero = int(input("Cuantos articulos has comprado? "))
dinero = int(input("Cuanto has pagado? "))

precio_total = precio * numero
cambio = dinero - precio_total
print("El precio total era de {}€ y el cambio ha sido de {}€".format(precio_total,cambio))
"""

#5
"""
precio_pendientes = int(input("Cuanto valen los pendientes? "))
precio_pulseras = int(input("Cuanto valen las pulseras? "))
precio_mix = int(input("Cuanto vale el mix? "))

pulseras_vendidas = int(input("Cuantas pulseras se han vendido?"))
pendientes_vendidos = int(input("Cuantos pendientes se han vendido?"))
mix_vendidos = int(input("Cuantos mix se han vendido?"))

ganancia_pulsera = (pulseras_vendidas - mix_vendidos) * precio_pulseras
ganancia_pendientes = (pendientes_vendidos - mix_vendidos) * precio_pendientes
ganancia_mix = mix_vendidos * precio_mix
ganancia_total = ganancia_pendientes + ganancia_pulsera + ganancia_mix

print("Con las Pulseras ganó {}€, con los pendientes {}€ y con el pack {}€, un total de {}€".format(ganancia_pulsera, ganancia_pendientes, ganancia_mix, ganancia_total))
"""

