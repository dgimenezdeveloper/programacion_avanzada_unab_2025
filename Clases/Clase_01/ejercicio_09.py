""" Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el
precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado. """


def calculo_nuevo_precio(precio_anterior, porcentaje_aumento):
    """Calcula el nuevo precio dado el precio anterior y el porcentaje a aumentar."""
    if precio_anterior < 0:
        raise ValueError("El precio anterior debe ser mayor o igual a cero.")
    
    aumento = (porcentaje_aumento / 100) * precio_anterior
    nuevo_precio = precio_anterior + aumento
    
    return nuevo_precio