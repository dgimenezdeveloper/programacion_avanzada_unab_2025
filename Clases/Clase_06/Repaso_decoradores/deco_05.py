def imprimir_antes(mensaje):
    def decorador(function):
        def wrapper():
            print(mensaje)
            return function()  # Ejecuta la función decorada
        return wrapper
    return decorador

@imprimir_antes("¡Atención!")
def tarea_informativa():
    print("Realizando tarea...")

tarea_informativa()