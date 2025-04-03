""" Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad
de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del
transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión
sabiendo que cada salita es acompañada por tres adultos. """


def calculo_transporte(cant_alumnos_1era, cant_alumnos_2da, cant_alumnos_3era, cant_asientos_micro):
    """Calcula cuántos micros se necesitan para transportar a los alumnos."""
    
    cant_alumnos = cant_alumnos_1era + cant_alumnos_2da + cant_alumnos_3era
    cant_adultos = 3 * 3  # 3 salitas
    total_personas = cant_alumnos + cant_adultos
    
    micros_necesarios = total_personas // cant_asientos_micro
    if total_personas % cant_asientos_micro != 0:
        micros_necesarios += 1  # Si hay un residuo, se necesita un micro adicional
    
    return micros_necesarios