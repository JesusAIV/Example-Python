from boleta import Boleta
from time import sleep
import os

Trabajador1 = Boleta()
print("__________________________________")
print("      ______________________      ")
print("     |                      |     ")
print("     |    FERROTEK  S.A.C   |     ")
print("     |______________________|     ")
print("                                  ")
print("      *** DATOS DE ENTRADA ***    ")
print("                                  ")
Trabajador1.ObtenerDatos()
print("                                  ")
print("__________________________________")
print("\n")
if Trabajador1.Sueldo_Basico() > 0:
    print('Procesando boleta de pago...')
    sleep(2)
    os.system ("cls")

    print("__________________________________")
    print("      ______________________      ")
    print("     |                      |     ")
    print("     |    FERROTEK  S.A.C   |     ")
    print("     |______________________|     ")
    print("                                  ")
    print("      *** BOLETA DE PAGO ***      ")
    print("                                  ")
    print("    NOMBRE:              ", Trabajador1.trabajador.title())
    print("    CATEGORIA:           ", Trabajador1.categoria.upper())
    print("    SUELDO BASICO:       ", Trabajador1.Sueldo_Basico())
    print("    DESCUENTO TARDANZAS: ", round(Trabajador1.Descuento_Tardanzas(), 2))
    print("    PAGO HORAS EXTRAS:   ", round(Trabajador1.Pago_Extras(), 2))
    print("    SUELDO NETO:         ", round(Trabajador1.Sueldo_Neto(), 2))
    print("                                   ")
    print("___________________________________")

    input("PRESIONE ENTER PARA SALIR...")
else:
    print("CATEGORIA NO ENCONTRADA!!!")
