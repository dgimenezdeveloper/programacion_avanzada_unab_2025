#Programar preferentemente en Python la siguiente consigna utilizando funciones y parámetros:

# Calcular el área y el perímetro de un cuadrado, de un rectángulo y de una circunferencia.
# Realizar las invocaciones a las distintas funciones definidas anteriormente

# Usando POO

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2

class Circunferencia:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

# Instanciacion de clases y llamado a metodos
cuadrado = Cuadrado(5)
rectangulo = Rectangulo(10, 3)
circunferencia = Circunferencia(4)

print(f"El area del cuadrado es: {cuadrado.area()}")
print(f"El perimetro del cuadrado es: {cuadrado.perimetro()}")
print(f"El area del rectangulo es: {rectangulo.area()}")
print(f"El perimetro del rectangulo es: {rectangulo.perimetro()}")
print(f"El area de la circunferencia es: {circunferencia.area()}")
print(f"El perimetro de la circunferencia es: {circunferencia.perimetro()}")