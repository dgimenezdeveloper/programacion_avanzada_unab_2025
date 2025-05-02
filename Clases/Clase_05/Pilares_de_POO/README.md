# Participantes: Darío Giménez y Federico Paál

# ¿Cuáles son los 4 pilares de la programación orientada a objetos y qué aporta cada uno?

## Respuesta:

    Los 4 pilares de la programación orientada a objetos (POO) son:

- Abstracción:

  Permite ocultar los detalles complejos de implementación y mostrar solo las funcionalidades esenciales de un objeto.

- Encapsulamiento:

  Consiste en restringir el acceso directo a los datos de un objeto y permitir su manipulación solo a través de métodos definidos. Esto protege la integridad de los datos y mejora la modularidad del código.

- Herencia:

  Permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). Esto fomenta la reutilización del código y facilita la creación de jerarquías de clases.

- Polimorfismo:
  Permite que diferentes clases respondan de manera distinta al mismo método o mensaje.

# 1. ¿Cuál es la diferencia entre encapsulamiento y abstracción?

## Respuesta:

    El encapsulamiento protege los datos y controla el acceso a los mismos. En cambio, la abstracción se enfoca en oculatar los detalles de implementación y muestra las funcionalidades esenciales.

# 2. ¿Qué pilar permite a las subclases sobrescribir métodos?

    Polimorfismo. Este permite que una subclase redefina el comportamiento de un método heredado.

# Código con errores para corregir

```python
class Dog:
    def __init__(self, name):
        name = name

    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)

```

## Respuesta:

```python
class Dog:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog)

```

# Ejercicio:

Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método
