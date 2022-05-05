# Herencia única: permite que una clase derivado herede caracteristicas deuna sola clase principal
'''
class Empleado(): # Este es la clase padre
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class EmpleadoSupervisor(Empleado): # Este es la clase hija
    def __init__(self, nombre, edad, salario, id):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.id = id

empleado1 = Empleado("Jesús", 18, 12000)

print(empleado1.edad, "años")'''
class Estudiante: # Creamos la clase padre
    def __init__(self, edad, nombre): # Definimos los parametros edad y nombre
        self.edad = edad # Declaramos el atributo edad es igual al argumento
        self.nombre = nombre # Declaramos

class IngenieriaSoftware(Estudiante):
    def presentarse(self):
        print("Hola soy ", self.nombre, "Tengo ", self.edad, "años", "y estudio Ingenieria de Software con Inteligencia Artificial")

Jhon = IngenieriaSoftware(30, 'Jhon Doe')
Jhon.presentarse()