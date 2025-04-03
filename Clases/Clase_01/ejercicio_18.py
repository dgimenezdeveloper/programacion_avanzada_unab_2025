"""Ejercicio 18: En este código una fracción está representada por una lista de dos elementos, el
numerador y el denominador. Por ejemplo la fracción 3⁄4 sería la lista (3,4). Complete el código
según corresponda.
#Zona de definiciones de funciones
def cargarFraccion():
#Solicita al usuario el numerador y denominador. Arma la fracción como una lista y la retorna
... .
def numeradorFraccion(x):
#Retorna el numerador que se encuentra en la fracción x, representada como una lista
....
def denominadorFraccion(x):
#Retorna el denominador que se encuentra en la fracción x, representada como una lista
....
def sumaFracciones(x, y):
#Retorna la suma de las fracciones, representadas como listas
....
def restaFracciones(x, y):
#Retorna la resta de las fracciones, representadas como listas
....
def divisionFracciones(x, y)
#Retorna la división de las fracciones, representadas como listas:

....
def multiplicacionFracciones(x, y):
#Retorna la multiplicación fracciones, representadas como listas
....
#Zona del programa principal
print (“Bienvenidos/as a cuentas con Fracciones”)
a=cargarFraccion()
b=cargarFraccion()
print (“El denominador de la primera fracción es:”, .....)
print (“El numerador de la segunda fracción es:”, .....)
print (“La suma de dichas fracciones es:”, .....)
print (“La resta de dichas fracciones es:”, .....)
print (“La multiplicación de dichas fracciones es:”, .....)
print (“La división es:”, .....)"""


# Zona de definiciones de funciones
def cargarFraccion():
    """Solicita al usuario el numerador y denominador. Arma la fracción como una lista y la retorna"""
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    return [numerador, denominador]


def numeradorFraccion(x):
    """ Retorna el numerador que se encuentra en la fracción x, representada como una lista """
    return x[0]


def denominadorFraccion(x):
    """ Retorna el denominador que se encuentra en la fracción x, representada como una lista """
    return x[1]


def sumaFracciones(x, y):
    """  Retorna la suma de las fracciones, representadas como listas """
    return [
        numeradorFraccion(x) * denominadorFraccion(y)
        + numeradorFraccion(y) * denominadorFraccion(x),
        denominadorFraccion(x) * denominadorFraccion(y),
    ]


def restaFracciones(x, y):
    """ Retorna la resta de las fracciones, representadas como listas """
    return [
        numeradorFraccion(x) * denominadorFraccion(y)
        - numeradorFraccion(y) * denominadorFraccion(x),
        denominadorFraccion(x) * denominadorFraccion(y),
    ]


def divisionFracciones(x, y):
    """ Retorna la división de las fracciones, representadas como listas. """
    return [
        numeradorFraccion(x) * denominadorFraccion(y),
        denominadorFraccion(x) * numeradorFraccion(y),
    ]


def multiplicacionFracciones(x, y):
    """ Retorna la multiplicación fracciones, representadas como listas """
    return [
        numeradorFraccion(x) * numeradorFraccion(y),
        denominadorFraccion(x) * denominadorFraccion(y),
    ]


# Zona del programa principal
print("Bienvenidos/as a cuentas con Fracciones")
a = cargarFraccion()
b = cargarFraccion()
print("El denominador de la primera fracción es:", denominadorFraccion(a))
print("El numerador de la segunda fracción es:", numeradorFraccion(b))
print("La suma de dichas fracciones es:", sumaFracciones(a, b))
print("La resta de dichas fracciones es:", restaFracciones(a, b))
print("La multiplicación de dichas fracciones es:", multiplicacionFracciones(a, b))
print("La división es:", divisionFracciones(a, b))
