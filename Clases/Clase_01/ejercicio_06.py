""" Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
multiplicar de dicho número. """

def tabla_multiplicar(numero):
    """ Imprime la tabla de multiplicar del número dado. """
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        