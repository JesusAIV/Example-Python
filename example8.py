# Encapsulación

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_user(self):
        print('User Name is: ', self.name)
        print('User Age is: ', self.age)

user1 = User('Jhon Doe', 35)

# Llamando al método de la clase
user1.display_user()

# Accediendo directamente a las variables
user1.name