# 1. Aspectos conceptuales
    a) ¿Qué ventajas tiene la utilización de funciones?
        La utilización de funciones tiene varias ventajas:
        - Reutilización de código: una vez que se define una función, se puede utilizar en cualquier parte del programa.
        - Modularización: permite dividir el programa en partes más pequeñas y manejables.
        - Abstracción: permite ocultar los detalles de implementación de una función y solo mostrar su interfaz.
        - Facilidad de mantenimiento: si se necesita modificar una función, se puede hacer en un solo lugar.
        - Facilidad de lectura: al dividir el programa en funciones, se facilita la comprensión del código.
        - Facilidad de depuración: al dividir el programa en funciones, se facilita la identificación y corrección de errores.

    b) ¿Hay algún cuidado en el orden en el que se pasan los parámetros a una función?
        Si, el orden en el que se pasan los parámetros a una función es importante, ya que los parámetros se asignan a las variables formales en el mismo orden en el que se pasan. Por lo tanto, si se cambia el orden de los parámetros, se cambiará el valor de las variables formales.

    c) ¿Cuándo uso la sentencia return?
        La sentencia return se utiliza para devolver un valor desde una función. Se puede utilizar en cualquier parte del cuerpo de la función, pero una vez que se ejecuta, la función termina y devuelve el valor especificado. Si no se especifica un valor, la función devuelve **None**.

    d) ¿Qué diferencia hay entre la definición y la invocación de una función?
        La definición de una función es el proceso de crear una función y especificar su nombre, parámetros, cuerpo y valor de retorno. La invocación de una función es el proceso de llamar a una función y pasarle los parámetros necesarios. La definición de una función se realiza una sola vez, mientras que la invocación de una función se puede realizar varias veces.

    e) ¿Qué son los parámetros formales y para qué sirven? Ejemplifique.
        Los parámetros formales son los nombres de las variables que se utilizan en la definición de una función para representar los valores que se pasan a la función cuando se la invoca. Los parámetros formales sirven para definir la interfaz de la función y especificar los valores que se esperan recibir. Por ejemplo, en la función **def suma(a, b):**, **a** y **b** son parámetros formales que representan los valores que se pasan a la función cuando se la invoca.

    f) ¿Qué son los parámetros reales y para qué sirven? Ejemplifique.
        Los parámetros reales son los valores que se pasan a una función cuando se la invoca. Los parámetros reales sirven para proporcionar los valores necesarios para que la función realice su tarea. Por ejemplo, en la función **sum(5, 3)**, **5** y **3** son parámetros reales que se pasan a la función **sum** para realizar la suma.

    g) ¿Qué significa el cuerpo de una función? Ejemplifique.
        El cuerpo de una función es el bloque de código que se ejecuta cuando se invoca la función. Contiene las instrucciones que realizan la tarea de la función y pueden incluir declaraciones, expresiones, sentencias de control, llamadas a otras funciones, etc. Por ejemplo, en la función **def suma(a, b): return a + b**, el cuerpo de la función es **return a + b** que realiza la suma de los parámetros **a** y **b** y devuelve el resultado.

    h) ¿Existen funciones sin parámetros o argumentos?
        Si, existen funciones sin parámetros o argumentos. Estas funciones no requieren valores de entrada para realizar su tarea y se definen sin parámetros formales. Por ejemplo, la función **def saludo(): print("Hola, mundo!")** no tiene parámetros y simplemente imprime un saludo en la consola.

    i) ¿Puede usar una letra o un número como parámetro formal? ¿Y como parámetro real?
        Si, se puede utilizar una letra o un número como parámetro formal en una función. Los parámetros formales son simplemente nombres de variables que representan los valores que se pasan a la función. Por ejemplo, en la función **def suma(a, b): return a + b**, **a** y **b** son parámetros formales que representan los valores que se pasan a la función. En cuanto a los parámetros reales, también se pueden utilizar letras o números, ya que son los valores que se pasan a la función cuando se la invoca. Por ejemplo, en la función **sum(5, 3)**, **5** y **3** son parámetros reales que se pasan a la función **sum**.
        Sin embargo, es importante tener en cuenta que los nombres de las variables deben seguir las reglas de nomenclatura de Python y no pueden ser palabras clave o nombres de funciones predefinidas, como así también ser autoexplicativos.

    j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una función?
        Si, se puede tener una cantidad distinta de parámetros formales que reales en una función. Python permite definir funciones con un número variable de parámetros formales utilizando el operador **\*** para indicar que se aceptan múltiples argumentos, o el operador **\*\*** para indicar que se aceptan múltos argumentos con nombre. Por ejemplo, la función **def suma(*args): return sum(args)** acepta un número variable de argumentos y devuelve la suma de todos ellos.
        En el caso de los parámetros reales, se pueden pasar más o menos valores de los que se esperan en la función, siempre y cuando se respeten las reglas de nomenclatura y los tipos de datos esperados por la función. Si se pasan más valores de los que se esperan, los valores adicionales se ignorarán. Si se pasan menos valores de los que se esperan, se generará un error de tipo **TypeError**.

    k) ¿Cómo se puede implementar un módulo con solo definiciones de funciones e importarlo desde tu programa? ¿Cuáles son las formas de importar que ofrece Python?
        Se puede implementar un módulo con solo definiciones de funciones creando un archivo con extensión **.py** que contenga las definiciones de las funciones. Luego, se puede importar el módulo desde otro programa utilizando la sentencia **import** seguida del nombre del módulo. Por ejemplo, si se tiene un módulo llamado **operaciones.py** con las definiciones de las funciones **suma** y **resta**, se puede importar el módulo en otro programa de la siguiente manera:
        ```python
        import operaciones
        resultado_suma = operaciones.suma(5, 3)
        resultado_resta = operaciones.resta(5, 3)
        print(resultado_suma, resultado_resta)
        ```
        Python ofrece varias formas de importar módulos:
        - **import module**: importa todo el módulo y se accede a las funciones y variables utilizando el nombre del módulo como prefijo.
        - **from module import function**: importa una función específica del módulo y se accede a ella directamente sin necesidad de usar el nombre del módulo como prefijo.
        - **from module import \***: importa todas las funciones y variables del módulo y se accede a ellas directamente sin necesidad de usar el nombre del módulo como prefijo.
        - **import module as alias**: importa el módulo con un alias o nombre corto y se accede a las funciones y variables utilizando el alias como prefijo.
        - **from module import function as alias**: importa una función específica del módulo con un alias y se accede a ella directamente utilizando el alias.
        - **from module import \* as alias**: importa todas las funciones y variables del módulo con un alias y se accede a ellas directamente utilizando el alias.

    l) ¿Qué diferencias hay entre los siguientes códigos?
        i) import math
            Esta línea importa el módulo **math** y permite acceder a todas las funciones y variables definidas en el módulo utilizando el prefijo **math**. Por ejemplo, para acceder a la función **sqrt** se debe escribir **math.sqrt**.
        ii) from math import sqrt
            Esta línea importa la función **sqrt** del módulo **math** y permite acceder a ella directamente sin necesidad de usar el prefijo **math**. Por ejemplo, para acceder a la función **sqrt** se puede escribir simplemente **sqrt**.
        Es recomendable utilizar la segunda forma cuando se necesita utilizar una función específica de un módulo, ya que evita la necesidad de usar el prefijo y hace que el código sea más legible, además de reducir la posibilidad de conflictos de nombres y no cargar el módulo completo si no es necesario.