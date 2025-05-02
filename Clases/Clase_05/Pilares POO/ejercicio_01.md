# Revisión de Programación Imperativa
## Pregunta teórica:
- ¿Qué caracteriza a la programación imperativa y en qué se diferencia de la programación
declarativa?
    
    La programación imperativa se basa en describir cómo se debe realizar una tarea, utilizando
    instrucciones secuenciales y estructuras de control como bucles y condicionales.
    
    La programación declarativa se centra en describir qué se quiere lograr, sin
    especificar cómo se debe hacer. En la programación declarativa, el enfoque está en el
    resultado final, mientras que en la programación imperativa se detalla el proceso paso a
    paso para alcanzar ese resultado.


1. ¿Verdadero o falso? La programación imperativa se basa en describir qué se quierelograr, no cómo.

    Falso. La programación imperativa se basa en describir cómo se debe realizar una tarea,
    utilizando instrucciones secuenciales y estructuras de control como bucles y condicionales.
    
    La programación declarativa es la que se centra en describir qué se quiere lograr,
    sin especificar cómo se debe hacer.


2. ¿Qué estructuras básicas componen la programación imperativa?


    - Estructuras de control: Permiten tomar decisiones y repetir acciones (if, for, while).
    - Funciones: Bloques de código reutilizables que realizan tareas específicas.
    - Entrada y salida: Mecanismos para interactuar con el usuario o el sistema (input, print).


## Código con errores para corregir
### Código con mal uso del bucle y sin claridad
```python
nums = [1,2,3,4]
for i in nums:
    if i % 2 == 0:
        i = i * 2
    print(i)
```

**Errores:**
- El bucle no está modificando la lista original, solo está duplicando los números pares
  temporalmente.
- La salida no es clara, ya que imprime todos los números, no solo los pares duplicados.
- La variable `i` se usa para iterar y también para almacenar el resultado, lo que puede
  causar confusión.

**Corrección**
```python
nums = [1,2,3,4]
result = []
for i in nums:
    if i % 2 == 0:
        result.append(i * 2)
    else:
        result.append(i)
print(result)
```


## Reflexión individual
- ¿Qué diferencias notaste entre escribir código imperativo y usar comprensiones o funciones como map o filter?
Al escribir código imperativo, se requiere más atención a los detalles y la lógica de control
de flujo, lo que puede hacer que el código sea más extenso y menos legible. En cambio, al usar
comprensiones, el código se vuelve más conciso y legible, ya que se enfoca en la transformación de datos en lugar de en el proceso de control. 