# METACLASES

* Las metaclases son clases que crean clases.
* En Python, todo es un objeto, incluidas las clases.
* Las metaclases permiten personalizar la creación de clases, lo que puede ser útil para implementar patrones de diseño, validaciones o comportamientos específicos en la creación de clases.
* Se definen como una subclase de `type`.
* La metaclase se utiliza al crear una clase, y se puede especificar mediante el argumento `metaclass` en la definición de la clase.
* La metaclase puede modificar la clase antes de que se cree, lo que permite agregar atributos, métodos o realizar validaciones.
* La metaclase predefinida en Python es `type`, que se utiliza para crear todas las clases en Python.
* La estructura de una metaclase es similar a la de una clase normal, pero en lugar de definir métodos de instancia, se definen métodos de clase.
* Los métodos más comunes en una metaclase son `__new__` y `__init__`.
  * `__new__`: Se encarga de crear la instancia de la clase.
  * `__init__`: Se encarga de inicializar la instancia creada por `__new__`.
* La metaclase se puede utilizar para:
  * Validar atributos de clase.
  * Agregar métodos o atributos a la clase.
  * Modificar el comportamiento de la clase al momento de su creación.
  * Implementar patrones de diseño como Singleton, Factory, etc.

## Sintaxis para type()

```python
class MiClase(metaclass=type):
    pass
```
* `MiClase` es la clase que se está definiendo.
* `metaclass=type` indica que la metaclase utilizada para crear `MiClase` es `type`.