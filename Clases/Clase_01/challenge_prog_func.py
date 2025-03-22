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