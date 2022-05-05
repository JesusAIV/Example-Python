# Escribir un programa en python para crear una clase Vehicule con atributos de instancia. max_speed milage(max velocidad y kilometraje)

from xml.parsers.expat import model


class Vehicule:

    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

modelotoyota = Vehicule(240, 20)
print("La velocidad del vehiculo es km/h: ", modelotoyota.max_speed)
print("El kilometraje recorrido por toyota es: ", modelotoyota.milage)