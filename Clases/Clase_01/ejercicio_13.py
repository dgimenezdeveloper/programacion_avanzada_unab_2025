""" Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el
monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le
toca pagar a cada uno. """

def a_pagar(cantidad_personas, bebida, comida, alquiler):
    """Calcula cuánto le toca pagar a cada persona."""
    
    if cantidad_personas <= 0:
        raise ValueError("La cantidad de personas debe ser mayor que cero.")
    
    total_gasto = bebida + comida + alquiler
    gasto_por_persona = total_gasto / cantidad_personas
    
    return gasto_por_persona