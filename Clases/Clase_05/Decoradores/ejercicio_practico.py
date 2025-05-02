"""Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user
tiene el atributo is_admin=True.
Si no, debe imprimir “Acceso denegado”.
Prueba el decorador con una función de ejemplo."""


# Definición del decorador
def authorize(funcion):
    def wrapper(user):
        if user.__is_admin:
            return funcion(user)
        else:
            print("Acceso denegado")

    return wrapper


class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.__is_admin = is_admin

    def __str__(self):
        return f"User: {self.name}, Admin: {self.is_admin}"

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

    def set_is_admin(self, is_admin):
        self.__is_admin = is_admin
        return self.is_admin

    def get_is_admin(self):
        return self.is_admin


# Ejemplo de uso del decorador
@authorize
def funcion_protegida(user):
    print(f"Acceso concedido a {user.name}")


# Creación de usuarios
user1 = User("Fede", True)
user2 = User("Daro", False)

# Ejecución de la función protegida
funcion_protegida(user1)  # Imprime: Acceso concedido a Juan
funcion_protegida(user2)  # Imprime: Acceso denegado


# Ejemplo de uso del decorador
@authorize
def funcion_protegida(user):
    print(f"Acceso concedido a {user.name}")
    return f"Función ejecutada por {user.name}"

