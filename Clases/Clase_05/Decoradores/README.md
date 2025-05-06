# Participantes: Darío Giménez y Federico Paál

# ¿Qué es un decorador en Python y para qué se utiliza comúnmente?

## Respuestas:

    Un decorador en Python es una función que toma otra función (u objeto invocable) como argumento y devuelve una nueva función con funcionalidad adicional, sin modificar directamente el código de la función original.

Los decoradores se usan principalmente para:

- Añadir comportamiento antes o después de una función, como logging, control de acceso, temporización, validación, etc.

- Reutilizar código sin necesidad de duplicarlo.

- Registrar funciones (por ejemplo, en frameworks como Flask o Django).

- Transformar funciones o métodos de forma elegante y legible.

# 1. ¿Como se aplica a una función?

## Respuesta:

    Se la aplica a una función, utilizando un @ seguido del nombre del decorador por sobre la función.

# 2. ¿Qué función interna suele tener un decorador?

    Como función interna posee un "wrapper" el cual se utiliza para envolver la función decoradorada.

# Código con errores para corregir

## Respuesta:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorating...")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

@decorator
def greet():
    print("Hi!")
greet()
```

# Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user

tiene el atributo is_admin=True. Si no, debe imprimir“Acceso denegado”. Prueba el decorador con una función de ejemplo
