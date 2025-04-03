""" Ejercicio 17:
a) Definir una función que reciba como parámetro una lista de números y retorne la suma del
primer elemento con el último.
#Zona de definiciones de funciones
def sumaPrimUlt(lis):
#retorna la suma entre el primer elemento de la lista con el último
....
def promedioPrimUlt(lis):
#retorna el promedio entre el primer elemento de la lista con el último
....
#Zona del programa principal
#solicitar al usuario 3 números, armar la lista e invocar las funciones anteriores mostrando los #resultados
..... """

# Definición de la función que suma el primer y último elemento de la lista
def sumaPrimUlt(lis):
    """Retorna la suma entre el primer elemento de la lista con el último."""
    if len(lis) == 0:
        raise ValueError("La lista no puede estar vacía.")
    
    return lis[0] + lis[-1]


# Definición de la función que calcula el promedio entre el primer y último elemento de la lista
def promedioPrimUlt(lis):
    """Retorna el promedio entre el primer elemento de la lista con el último."""
    if len(lis) == 0:
        raise ValueError("La lista no puede estar vacía.")
    
    return (lis[0] + lis[-1]) / 2

def mostrarResultados(suma, promedio):
    """Muestra los resultados de la suma y el promedio."""
    print(f"La suma del primer y último elemento es: {suma}")
    print(f"El promedio del primer y último elemento es: {promedio}")

# Programa principal
def main():

    numeros = []
    for i in range(3):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
        
    suma = sumaPrimUlt(numeros)
    promedio = promedioPrimUlt(numeros)
    
    mostrarResultados(suma, promedio)

if __name__ == "__main__":
    main()
