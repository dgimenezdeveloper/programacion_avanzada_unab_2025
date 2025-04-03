""" Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto
dado su precio de venta sin IVA. """


def precio_con_iva(precio_sin_iva):
    if precio_sin_iva < 0:
        raise ValueError("El precio sin IVA debe ser mayor o igual a cero.")
    iva = 0.21
    precio_con_iva = precio_sin_iva + (precio_sin_iva * iva)
    return precio_con_iva