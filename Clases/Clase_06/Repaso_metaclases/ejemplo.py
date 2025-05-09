class User:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def create_admin(self):
    return f'admin {self.nombre} creado'

Admin = type("Admin", (User,),{"create_admin": create_admin})

def correr(self):
    print('Estoy corriendo')
    
def __str__(self):
    return f'Soy {self.nombre}'
    
Animal = type('Perro',(), {'nombre': 'Demian', 'correr':correr})
Gato = type('Mascota',(Animal,),dict(nombre="Dash", correr=correr))


a = Animal()

b = Gato()

print(a.nombre)
print(type(a))
a.correr()

print(b.nombre)
b.correr()
