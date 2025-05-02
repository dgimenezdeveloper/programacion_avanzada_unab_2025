def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorating...")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper
    
@decorator
def greet():
    print("Hi!")
#greet()


class User:
    def __init__(self, is_admin):
        self.__is_admin = is_admin

    def get_admin(self):
        return self.__is_admin

def authorize(func):
    def wrapper(user):
        if user.get_admin():
            print("Acceso concedido")
            return func(user)
        else:
            print("Acceso denegado")
    return wrapper

user_1 = User(True)
user_2 = User(False)

@authorize
def login(user):
    print("Bienvenido usuario_1")

login(user_1)
