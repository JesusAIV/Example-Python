# Crear una clase con instancia de atributos

class Employee:
    # Definiendo las propiedades y asignando valores
    id_employee = 5
    salario = 2000
    departamento = "Recursos humanos"
    horario = "diurno"

# Crear un objeto de la clase Employee
Saul = Employee()

# Imprimir las propiedades de Saul
print("id = ", Saul.id_employee) # Objeto.Propiedad
print("Salario de Saul = ", Saul.salario)
print("Departamento = ", Saul.departamento)
print("Horario = ", Saul.horario)