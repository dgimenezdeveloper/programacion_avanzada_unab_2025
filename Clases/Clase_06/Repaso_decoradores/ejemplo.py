import time

def calcular_tiempo(funcion):
    def wrapper(*args,**kwargs):
        inicio =  time.time()
        funcion(*args,**kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin-inicio} segundos")
    return wrapper
        



@calcular_tiempo
def imiprimirNumeros(n):
    for i in range(n):
        print(i)

#imiprimirNumeros(1000)


def imprimirMensaje(funcion):
    def wrapper(a,b):
        resultado = funcion(a,b)
        print(f'La suma fue de: {resultado}')
    return wrapper
        
@imprimirMensaje
def suma(a,b):
    return a+b

#suma(2,4)
