# Escribir un programa en python para crear una clase articulo con atributos de instancia: código del articulo, cantidad,precio.
# Métodos: mostrar la cantidad actual, mostrar el precio, reducir la cantidad actual, incrementa la cantidad actual.
class Articulo:
    def __init__(self, codigo, cantidad, precio):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio
    def CantidadActual(self):
        print("Cantidad: ", self.cantidad)
    def MostrarPrecio(self):
        print("Precio: ", self.precio)
    def ReducirCantidad(self, newcantidad):
        self.cantidad = self.cantidad - newcantidad
        print("Cantidad reducida a: ", self.cantidad)
    def IncremetaCantidad(self, newcantidad):
        self.cantidad = self.cantidad + newcantidad
        print("Cantidad aumentada a: ", self.cantidad)

articulo1 = Articulo(65468465, 50, 25)
print("Codigo: ", articulo1.codigo)
articulo1.CantidadActual()
articulo1.MostrarPrecio()
articulo1.ReducirCantidad(20)
articulo1.IncremetaCantidad(50)