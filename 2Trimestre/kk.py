# class Coche:
#     def __init__(self,marca,modelo):
#         self.marca = marca
#         self.modelo = modelo
#         self.encendido = False

#     def arrancar(self):
#         self.encendido = True
#         print(f"El coche {self.marca} {self.modelo} está arrancado.")

# mi_coche = Coche("Toyota", "Corolla")
# mi_coche.arrancar()



class Ave:
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color
        self.volando = False

    def volar(self):
        self.volando = True
        print(f"El ave {self.especie} de color {self.color} está volando.")

class Pinguino(Ave):
    def volar(self):
        print(f"El pingüino {self.especie} no puede volar.")    

mi_ave = Ave("Loro", "Verde")
mi_ave.volar()
mi_pinguino = Pinguino("Emperador","Verde")
mi_pinguino.volar()