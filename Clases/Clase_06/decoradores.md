# Decoradores en Python

**Ejercicio 1:**

Escribe un decorador `mostrar_ejecucion` que simplemente imprima la cadena "La función fue ejecutada." antes de llamar a la función decorada. Aplica `@mostrar_ejecucion` a una función llamada `saludar_simple()` que imprima "¡Hola!".

**Ejercicio 2:**

Escribe un decorador `envolver_parentesis` que tome la salida de la función decorada (que se espera que sea una cadena) y la envuelva entre paréntesis. Aplica `@envolver_parentesis` a una función llamada `obtener_texto()` que retorna la cadena "un texto".

**Ejercicio 3:**

Escribe un decorador `convertir_mayusculas` que tome la salida de la función decorada (que se espera que sea una cadena) y la convierta a mayúsculas antes de retornarla. Aplica `@convertir_mayusculas` a una función llamada `obtener_minuscula()` que retorna la cadena "texto en minúsculas".

**Ejercicio 4:**

Escribe un decorador `agregar_exclamacion` que tome la salida de la función decorada (que se espera que sea una cadena) y le agregue un signo de exclamación al final. Aplica `@agregar_exclamacion` a una función llamada `obtener_saludo()` que retorna la cadena "Buenos días".

**Ejercicio 5:**

Escribe un decorador `imprimir_antes` que tome un argumento de cadena `mensaje`. Antes de ejecutar la función decorada, el decorador debe imprimir el `mensaje`. Aplica `@imprimir_antes("¡Atención!")` a una función llamada `tarea_informativa()` que simplemente imprime "Realizando tarea...".


**Ejercicio 6:**

Escribe un decorador `saludar` que imprima "¡Hola!" antes de llamar a la función decorada y luego ejecute la función. Aplica `@saludar` a una función llamada `presentarse()` que simplemente imprime "Soy una función.".

**Ejercicio 7:**

Escribe un decorador `medir_tiempo` que calcule el tiempo que tarda en ejecutarse la función decorada. Deberá imprimir "La función tardó X segundos en ejecutarse." al finalizar la ejecución y retornar el resultado de la función. Aplica `@medir_tiempo` a una función llamada `tarea_larga()` que simule una operación que toma varios segundos (por ejemplo, usando `time.sleep()`).

**Ejercicio 8:**

Escribe un decorador `envolver_en_html` que tome un argumento `tag` (por defecto "div") y envuelva el resultado de la función decorada en etiquetas HTML `<tag>...</tag>`. Aplica `@envolver_en_html()` a una función llamada `obtener_nombre()` que retorna una cadena con un nombre. Prueba a aplicarlo con y sin especificar el argumento `tag`.

**Ejercicio 9:**

Escribe un decorador `solo_positivos` que reciba una función que toma argumentos numéricos. El decorador debe verificar que todos los argumentos pasados a la función sean positivos. Si alguno no lo es, debe imprimir un mensaje de error y no ejecutar la función original. Si todos son positivos, debe ejecutar la función y retornar su resultado. Aplica `@solo_positivos` a una función llamada `multiplicar(a, b)` que retorna el producto de sus argumentos.

**Ejercicio 10:**

Escribe un decorador `contar_llamadas` que mantenga un registro de cuántas veces se ha llamado a la función decorada. Deberá imprimir un mensaje cada vez que se llame a la función, indicando el número de veces que ha sido invocada hasta el momento, y luego ejecutar la función. Aplica `@contar_llamadas` a una función simple llamada `hacer_algo()` que imprima un mensaje. Llama a la función decorada varias veces para verificar el contador.

