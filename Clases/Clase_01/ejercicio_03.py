""" 
Ejercicio 3: Definir una función denominada retorno_mensaje que retorne siguiente mensaje:
“Estudiando en la UNAB”.
A. ¿Cómo hago para mostrar ese mensaje en pantalla?
B. ¿Qué diferencia encuentra con el ejercicio anterior?
C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAB“ y
“Estudiando Python en la UNAB” utilizando la misma función ¿Cómo la modificarías?
"""
def retorno_mensaje():
    return "Estudiando en la UNAB"

# A. Para mostrar el mensaje en pantalla, se debe llamar a la función y luego imprimir el valor retornado
print(retorno_mensaje())

# B. La diferencia con el ejercicio anterior es que en este caso la función retorna un valor, 
# mientras que en el ejercicio anterior la función solo imprimía un mensaje en pantalla.

# C. Para imprimir mensajes como “Estudiando Matemática I en la UNAB“ y “Estudiando Python en la UNAB”
# utilizando la misma función, se puede modificar la función para que reciba un parámetro que indique
# la materia que se está estudiando. De la siguiente forma:
def retorno_mensaje(materia):
    return f"Estudiando {materia} en la UNAB"

print(retorno_mensaje("Matemática I"))
print(retorno_mensaje("Python"))
