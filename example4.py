# Escribir un programa en python para crear una clase cuenta bancaria con atributos de instancia, numero de cuenta, nombre del titular, balance
'''
class CuentaBancaria:

    def __init__(self, NumCuenta, NomTitular, balance):
        self.NumCuenta = NumCuenta
        self.NomTitular = NomTitular
        self.balance = balance

cuentadebanco = CuentaBancaria(41500051234567, "Sheyla", 240)
print("Numero de cuenta   : ", cuentadebanco.NumCuenta)
print("Nombre del titular : ", cuentadebanco.NomTitular)
print("Balance            : ", cuentadebanco.balance)
'''


# Metodos o funcionalidades: retirar, depositar, generar balance, actualizar datos, ...
class CuentaBancaria:

    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
    def generar_balance(self):
        print(self.balance)
    def depositar(self, monto):
        if monto > 0:
            self.balance = self.balance + monto

cuenta1 = CuentaBancaria(41500051234567, "Sheyla", 5000)

cuenta1.generar_balance()
cuenta1.depositar(500)
cuenta1.generar_balance()
cuenta1.depositar(400)
cuenta1.generar_balance()

'''
print("Numero de cuenta   : ", cuentadebanco.NumCuenta)
print("Nombre del titular : ", cuentadebanco.NomTitular)
print("Balance            : ", cuentadebanco.balance)
'''