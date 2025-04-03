""" Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para la
cantidad de días que debe suministrar el remedio, el segundo dato para la cantidad de veces por
día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La
función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza. """

def calculo_dosis(cantidad_dias, veces_por_dia, comprimidos_por_envase):
    """Calcula si el envase de comprimidos alcanza para el tratamiento."""
    
    comprimidos_necesarios = cantidad_dias * veces_por_dia
    
    if comprimidos_necesarios <= comprimidos_por_envase:
        return True  # El envase alcanza
    else:
        return False  # El envase no alcanza
    