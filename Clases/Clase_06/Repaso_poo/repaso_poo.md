# Repaso de POO en Python
### Ejercicio 1:

Define en Python dos clases:

Animal: con atributo nombre (string) y método emitir_sonido() que imprime "Sonido genérico de animal".
Perro: hereda de Animal y redefine el método emitir_sonido() para imprimir "¡Guau!".

### Ejercicio 2:

Define en Python dos clases:

Figura: con atributo color (string) y método area() que devuelve 0 (ya que es una figura genérica).
Cuadrado: hereda de Figura, añade atributo lado (float) y redefine el método area() para calcular y devolver el área del cuadrado.

### Ejercicio 3:

Define en Python dos clases:

Empleado: con atributo nombre (string) y método calcular_salario() que devuelve un valor base de 1000.
Gerente: hereda de Empleado, añade atributo bono (float) y redefine el método calcular_salario() para añadir el bono al salario base.

### Ejercicio 4:

Define en Python dos clases:

Instrumento: con atributo tipo (string) y método tocar() que imprime "Sonido de instrumento genérico".
Guitarra: hereda de Instrumento y redefine el método tocar() para imprimir "¡Rasgueo de guitarra!".

### Ejercicio 5:

Define en Python dos clases:

Publicacion: con atributo titulo (string) y método mostrar_info() que imprime "Título: &lt;titulo>".
Libro: hereda de Publicacion, añade atributo autor (string) y redefine el método mostrar_info() para imprimir "Título: &lt;titulo>, Autor: &lt;autor>".

### Ejercicio 6:

Define en Python dos clases:

Dispositivo: con atributo nombre (string) y método encender() que imprime "<nombre> encendido".
Telefono: hereda de Dispositivo, añade atributo numero (string) y redefine el método encender() para imprimir "<nombre> (Número: &lt;numero>) encendido".

### Ejercicio 7:

Define en Python dos clases:

Producto: con atributo nombre (string) y método obtener_precio() que devuelve 0.
ProductoConDescuento: hereda de Producto, añade atributo descuento (float) y redefine obtener_precio() para aplicar el descuento a un precio base (por ejemplo, 100).

### Ejercicio 8:

Define en Python dos clases:

Forma: con método dibujar() que imprime "Dibujando una forma genérica".
Circulo: hereda de Forma, añade atributo radio (float) y redefine el método dibujar() para imprimir "Dibujando un círculo de radio <radio>".

### Ejercicio 9:

Define en Python dos clases:

CuentaBancaria: con atributo saldo (float) y método depositar(cantidad) que incrementa el saldo.
CuentaCorriente: hereda de CuentaBancaria y añade un atributo limite_sobregiro (float).

### Ejercicio 10:

Define en Python dos clases:

Electrodomestico: con atributo marca (string) y método informar() que devuelve "Electrodoméstico marca <marca>".
Lavadora: hereda de Electrodomestico, añade atributo capacidad (float) y redefine informar() para devolver "Lavadora marca <marca>, capacidad: <capacidad> kg".