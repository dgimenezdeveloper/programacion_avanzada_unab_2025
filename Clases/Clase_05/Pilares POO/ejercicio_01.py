""" 
🐀 Ejercicio práctico:
Crea una función que reciba una lista de números y devuelva otra lista con solo los números
pares multiplicados por 3, usando solo estructuras imperativas (no comprensiones ni
funciones como map o filter).
🐀 Reflexión individual
¿Qué diferencias notaste entre escribir código imperativo y usar comprensiones o funciones
como map o filter?
🐀 Desafío opcional
Convertí el mismo ejercicio imperativo a uno declarativo (usando list comprehension) y
compará claridad y legibilidad.
"""

# Código corregido
nums = [1, 2, 3, 4]
result = []

for i in nums:
    if i % 2 == 0:
        result.append(i * 2)
    else:
        result.append(i)

print(result)  # Salida: [1, 4, 3, 8]

################################################################

""" Crea una función que reciba una lista de números y devuelva otra lista con solo los números
pares multiplicados por 3, usando solo estructuras imperativas (no comprensiones ni
funciones como map o filter). """


def procesar_pares(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0: 
            resultado.append(numero * 3)
    
    return resultado


numeros = [1, 2, 3, 4, 5, 6]
resultado = procesar_pares(numeros)
print(resultado)

""" Desafío opcional
Convertí el mismo ejercicio imperativo a uno declarativo (usando list comprehension) y
compará claridad y legibilidad.
 """

# Programación declarativa (usando list comprehension)
def procesar_pares(lista):
    return [i*3 for i in lista if i % 2==0]

numeros = [1, 2, 3, 4, 5, 6]
resultado = procesar_pares(numeros)
print(resultado)