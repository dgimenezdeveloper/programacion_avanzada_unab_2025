# Refactorización de una Aplicación Web Django: Un Enfoque Práctico de Diseño Orientado a Objetos

## Descripción

Este proyecto es el resultado de la refactorización de una aplicación web de revistería realizada con Django, aplicando los principios de la Programación Orientada a Objetos (POO) y patrones de diseño para lograr una solución más robusta, escalable y mantenible.

## Objetivos

- Eliminar duplicación de código en modelos, vistas y plantillas.
- Aplicar herencia, abstracción, polimorfismo y encapsulamiento.
- Mejorar la cohesión y reducir el acoplamiento.
- Adoptar buenas prácticas y patrones de diseño clásicos.

## Principales Cambios y Mejoras

### 1. Herencia y Abstracción

- Se creó una clase abstracta `Producto` en [`tienda/models.py`](RevisteriaProyecto/tienda/models.py) que encapsula los campos y comportamientos comunes.
- Las clases `Libro` y `Merchandising` heredan de `Producto`, eliminando la duplicación.

### 2. Polimorfismo y Vistas Genéricas

- Se implementaron Vistas Basadas en Clases (CBV) como [`ProductoListView`](RevisteriaProyecto/tienda/views.py) y [`IndexView`](RevisteriaProyecto/tienda/views.py), que permiten listar diferentes tipos de productos de forma polimórfica según la categoría.
- Las URLs son dinámicas y reutilizables, por ejemplo: `/productos/<categoria>/`.

### 3. Encapsulamiento

- Toda la lógica del carrito de compras está centralizada en la clase [`Carrito`](RevisteriaProyecto/tienda/carrito.py), que gestiona agregar, restar, eliminar y limpiar productos, operando sobre la sesión del usuario.

### 4. Reutilización de Código y Mixins

- Se creó el mixin [`StaffRequiredMixin`](RevisteriaProyecto/tienda/views.py) para restringir el acceso a vistas administrativas, reutilizando lógica de permisos sin duplicación.

### 5. Mejora de la Interfaz

- Plantillas unificadas y uso de Bootstrap 5 para un diseño moderno y responsivo.
- Formularios renderizados con django-crispy-forms para una mejor experiencia de usuario.

### 6. Patrones de Diseño Aplicados

- **Template Method:** Las CBV de Django permiten personalizar pasos del algoritmo sobrescribiendo métodos como `get_queryset()`.
- **Factory:** Selección dinámica de formularios en vistas de creación/edición de productos.
- **Singleton (conceptual):** El carrito mantiene un único estado por sesión de usuario.

## Instalación

### 1. Clona el repositorio

```sh
git clone <url-del-repo>
cd RevisteriaProyecto
```

### 2. Crea un entorno virtual

#### En Windows

```bat
python -m venv venv
venv\Scripts\activate
```

#### En Linux/MacOS

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```sh
pip install -r requirements.txt
```

### 4. Realiza las migraciones

```sh
python manage.py migrate
```
o, en Linux/MacOS:
```sh
python3 manage.py migrate
```

### 5. Crea un superusuario

```sh
python manage.py createsuperuser
```
o, en Linux/MacOS:
```sh
python3 manage.py createsuperuser
```

### 6. Ejecuta el servidor de desarrollo

```sh
python manage.py runserver
```
o, en Linux/MacOS:
```sh
python3 manage.py runserver
```

---

Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/)

## Estructura del Proyecto

- [`RevisteriaPro/`](RevisteriaProyecto/RevisteriaPro): Configuración principal de Django.
- [`tienda/`](RevisteriaProyecto/tienda): Modelos, vistas, formularios, lógica de carrito y plantillas.
- [`media/`](RevisteriaProyecto/media): Imágenes de productos.
- [`static/`](RevisteriaProyecto/tienda/static): Archivos estáticos (CSS, JS, imágenes).
- [`templates/`](RevisteriaProyecto/tienda/templates): Plantillas HTML.

## Créditos

- Nahuel Dalesio
- Darío Giménez
- Federico Paál

## Enlace al informe y presentación

El informe completo y la presentación se encuentran en la carpeta raíz del repositorio.

---


¡Gracias por visitar La Antigua Revistería! Esperamos que este proyecto te inspire a aplicar POO y patrones de diseño en tus propias aplicaciones Django.