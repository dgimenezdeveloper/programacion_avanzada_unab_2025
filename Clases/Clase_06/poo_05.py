"""
### Ejercicio 5:

Define en Python dos clases:

Publicacion: con atributo titulo (string) y método mostrar_info() que imprime "Título: &lt;titulo>".
Libro: hereda de Publicacion, añade atributo autor (string) y 
	redefine el método mostrar_info() para imprimir "Título: &lt;titulo>, Autor: &lt;autor>".
"""

class Publicacion():
	def __init__(self, titulo):
		self.__titulo = titulo

	def mostrar_info(self):
		print(f"Titulo: {self.__titulo}")

class Libro(Publicacion):
	def __init__(self, titulo, autor):
		super().__init__(titulo)
		self.__autor = autor

	def mostrar_info(self):
		print(f"Titulo: {self._Publicacion__titulo}, Autor: {self.__autor}")
		
publicacion = Publicacion("Harry Potter")
publicacion.mostrar_info()

libro = Libro("Harry Potter", "J.K. Rowling")
libro.mostrar_info()