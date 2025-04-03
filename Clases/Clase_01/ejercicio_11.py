""" Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres (para el
nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima
un cartel de la siguiente forma:
*************************************
Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
Antes: precio anterior (dato recibido como parámetro)
Ahora: precio rebajado (dato recibido como parámetro) """

def armo_cartel(nombre_producto, precio_anterior, precio_rebajado):
    """Imprime un cartel de rebaja para un producto dado su nombre y precios."""
    
    if precio_anterior <= 0:
        raise ValueError("El precio anterior debe ser mayor que cero.")
    
    if precio_rebajado < 0:
        raise ValueError("El precio rebajado no puede ser negativo.")
    
    print("*" * 37)
    print(f"Atención!!! Gran rebaja para el producto {nombre_producto}")
    print(f"Antes: ${precio_anterior:.2f}")
    print(f"Ahora: ${precio_rebajado:.2f}")
    print("*" * 37)
    print()