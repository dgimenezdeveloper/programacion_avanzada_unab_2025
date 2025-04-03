"""Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de un
rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir
dichas funciones."""

import math


def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio**2


def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura


def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado su lado."""
    return lado**2
