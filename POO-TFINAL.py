#La empresa FERROTEK SAC se dedica a la producción de balones de gas. Cuenta
#con trabajadores de la categoría A, B y C. El sueldo de los trabajadores y el pago por
#hora extra está en función de su categoría:
'''
class Empleado():
    def __init__(self,trabajador,categoria,horas_extras,tardanzas):
        self.trabajador = trabajador
        self.categoria = categoria
        self.horas_extras = horas_extras
        self.tardanzas = tardanzas
Tipo_Empleado =Empleado("Roberto","B",10,200)
#casefold()trabajador1= Empleado("Roberto Carlos","B",10,200)
print("Trabajador:",Tipo_Empleado.trabajador)
print("Categoria:",Tipo_Empleado.categoria)
print("Horas Extras:",Tipo_Empleado.horas_extras)
print("Tardanzas:",Tipo_Empleado.tardanzas)
'''

class Trabajador():
    def __init__(self):
        self.trabajador = None
        self.categoria = None
        self.horas_extras = None
        self.tardanzas = None

    def ObtenerDatos(self):
        self.trabajador = input("TRABAJADOR:              ")
        self.categoria = input("CATEGORIA:               ")
        self.horas_extras = float(input("HORAS EXTRAS:            "))
        self.tardanzas = float(input("TARDANZAS: (minutos)     "))

class Boleta(Trabajador):

    def sueldo_basico(self):
        if self.categoria == "A" or self.categoria == "a":
            sb = 3000
            return sb
        elif  self.categoria =="B" or self.categoria == "b":
            sb = 2500
            return sb
        elif self.categoria == "C" or self.categoria == "c":
            sb = 2000
            return sb
        else:
            sb = 0
            return sb

    def descuento_tardanzas(self):
        dsc = ((self.sueldo_basico()/240)/60)*self.tardanzas
        return dsc

    def pago_extras(self):
            comision = (self.sueldo_basico()/240)*self.horas_extras
            return comision
    def sueldo_neto(self):
        total =(self.sueldo_basico()+self.pago_extras()-self.descuento_tardanzas())
        return total

Trabajador1 = Boleta()
print("*** DATOS DE ENTRADA ***")
Trabajador1.ObtenerDatos()
if Trabajador1.sueldo_basico() > 0:
    print("\n*** BOLETA DE PAGO ***")
    print("Nombre:                 ",Trabajador1.trabajador)
    print("Categoria:              ",Trabajador1.categoria)
    print("Sueldo Basico:          ",Trabajador1.sueldo_basico())
    print("Descuento Tardanzas:    ",round(Trabajador1.descuento_tardanzas(), 2))
    print("Pago horas extras:      ",round(Trabajador1.pago_extras(), 2))
    print("Sueldo Neto:            ",round(Trabajador1.sueldo_neto(), 2))
else:
    print("Categoria no encontrada")


'''
Tipo_Empleado =Trabajador("Jesus Alberto","B",10,200)

print("Trabajador:",Tipo_Empleado.trabajador)
print("Categoria:",Tipo_Empleado.categoria)
print("Horas Extras:",Tipo_Empleado.horas_extras)
print("Tardanzas:",Tipo_Empleado.tardanzas)
#Datos de Boleta
Trabajador1 = Trabajador("Jesus Alberto","B",10,200)
print("Nombre:",Trabajador1.trabajador)
print("Categoria:",Trabajador1.categoria)
print("Sueldo Basico:",Trabajador1.sueldo_basico())
print("Descuento Tardanzas: ",Trabajador1.descuento_tardanzas())
print("Pago horas extras:",Trabajador1.pago_extras())
print("Sueldo Neto:",Trabajador1.sueldo_neto())
'''