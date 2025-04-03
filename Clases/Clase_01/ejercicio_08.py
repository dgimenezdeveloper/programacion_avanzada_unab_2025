"""Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio
anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje
rebajado."""


def calculo_rebaja(precio_anterior, precio_rebajado):
    """Calcula el porcentaje de rebaja dado el precio anterior y el precio rebajado."""
    if precio_anterior <= 0:
        raise ValueError("El precio anterior debe ser mayor que cero.")
    
    rebaja = precio_anterior - precio_rebajado
    porcentaje_rebaja = (rebaja / precio_anterior) * 100
    
    return porcentaje_rebaja