""" Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto, ancho y
profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene. """


def calculo_litros(alto, ancho, profundidad):
    """Calcula la cantidad de litros de una pileta dada su altura, ancho y profundidad."""
    
    volumen_m3 = alto * ancho * profundidad
    litros = volumen_m3 * 1000
    return litros