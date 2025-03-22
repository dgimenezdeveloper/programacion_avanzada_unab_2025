""" Programar preferentemente en Python la siguiente consigna utilizando funciones y parámetros:

# Calcular el área y el perímetro de un cuadrado, de un rectángulo y de una circunferencia.
# Realizar las invocaciones a las distintas funciones definidas anteriormente. """

# Definicion de funciones
def area_cuadrado(lado):
    return lado * lado

def perimetro_cuadrado(lado):
    return lado * 4

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return (base + altura) * 2

def area_circunferencia(radio):
    return 3.1416 * radio ** 2

def perimetro_circunferencia(radio):
    return 2 * 3.1416 * radio

# Invocacion de funciones
lado = 5
base = 10
altura = 3
radio = 4

print(f"El area del cuadrado es: {area_cuadrado(lado)}")
print(f"El perimetro del cuadrado es: {perimetro_cuadrado(lado)}")
print(f"El area del rectangulo es: {area_rectangulo(base, altura)}")
print(f"El perimetro del rectangulo es: {perimetro_rectangulo(base, altura)}")
print(f"El area de la circunferencia es: {area_circunferencia(radio)}")
print(f"El perimetro de la circunferencia es: {perimetro_circunferencia(radio)}")

# Fin del programa

# Usando POO

class Figura:
    def __init__(self, lado, base, altura, radio):
        self.lado = lado
        self.base = base
        self.altura = altura
        self.radio = radio

    def area_cuadrado(self):
        return self.lado ** 2

    def perimetro_cuadrado(self):
        return self.lado * 4

    def area_rectangulo(self):
        return self.base * self.altura

    def perimetro_rectangulo(self):
        return (self.base + self.altura) * 2

    def area_circunferencia(self):
        return 3.1416 * self.radio ** 2

    def perimetro_circunferencia(self):
        return 2 * 3.1416 * self.radio
    
figura = Figura(5, 10, 3, 4)
print(f"El area del cuadrado es: {figura.area_cuadrado()}")
print(f"El perimetro del cuadrado es: {figura.perimetro_cuadrado()}")
print(f"El area del rectangulo es: {figura.area_rectangulo()}")
print(f"El perimetro del rectangulo es: {figura.perimetro_rectangulo()}")
print(f"El area de la circunferencia es: {figura.area_circunferencia()}")
print(f"El perimetro de la circunferencia es: {figura.perimetro_circunferencia()}")
# Fin del programa