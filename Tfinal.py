class Trabajador(): # Clase "Trabajador"
    def __init__(self):
        self.trabajador = None
        self.categoria = None
        self.horas_extras = None
        self.tardanzas = None

    #Metodos
    def ObtenerDatos(self): # Metodo "ObtenerDatos"
        self.trabajador = input("TRABAJADOR:                ")
        self.categoria = input("CATEGORIA:                 ")
        self.horas_extras = float(input("HORAS EXTRAS:              "))
        self.tardanzas = float(input("TARDANZAS: (minutos)       "))

# Clase Hijo
class Boleta(Trabajador): # Clase "Boleta"
    # Metodos
    def Sueldo_Basico(self): # Metodo "Sueldo_basico"
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

    def Descuento_Tardanzas(self): # Metodo "Descuento_tardanzas"
        dsc = ((self.Sueldo_Basico()/240)/60)*self.tardanzas
        return dsc

    def Pago_Extras(self): # Metodo "Pago_extras"
            comision = (self.Sueldo_Basico()/240)*self.horas_extras
            return comision
    def Sueldo_Neto(self): # Metodo "Sueldo_neto"
        total =(self.Sueldo_Basico()+self.Pago_Extras()-self.Descuento_Tardanzas())
        return total

Trabajador1 = Boleta()
print("*** DATOS DE ENTRADA ***")
Trabajador1.ObtenerDatos()
if Trabajador1.Sueldo_Basico() > 0:
    print("\n*** BOLETA DE PAGO ***")
    print("NOMBRE:                   ", Trabajador1.trabajador)
    print("CATEGORIA:                ", Trabajador1.categoria)
    print("SUELDO BASICO:            ", Trabajador1.Sueldo_Basico())
    print("DESCUENTO TARDANZAS:      ", round(Trabajador1.Descuento_Tardanzas(), 2))
    print("PAGO HORAS EXTRAS:        ", round(Trabajador1.Pago_Extras(), 2))
    print("SUELDO NETO:              ", round(Trabajador1.Sueldo_Neto(), 2))
else:
    print("CATEGORIA NO ENCONTRADA!!!")