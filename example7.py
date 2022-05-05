#class ClaseDerivada(ClaseA, CLaseB):
#    " Contenido de la clase "

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Instituto:
    def PresentarInstituto(self):
        print('Estudio en SENATI')

class InteligenciaArtificial(Estudiante, Instituto):
    def Presentarse(self):
        print("Hola soy ", self.nombre, "Tengo ", self.edad, "años y estudio Ingenieria de Software con Inteligencia Artificial")

Estudiante1 = InteligenciaArtificial('Jesus', 20)
Estudiante1.Presentarse()
Estudiante1.PresentarInstituto()