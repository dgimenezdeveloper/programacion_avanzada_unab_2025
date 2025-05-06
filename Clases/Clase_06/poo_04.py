"""
### Ejercicio 4:

Define en Python dos clases:

Instrumento: con atributo tipo (string) y método tocar() que imprime "Sonido de instrumento genérico".
Guitarra: hereda de Instrumento y redefine el método tocar() para imprimir "¡Rasgueo de guitarra!".
"""

class Instrumento():
	def __init__(self, tipo):
		self.__tipo = tipo

	def tocar(self):
		print("Sonido de instrumento genérico")

class Guitarra(Instrumento):
	def __init__(self, tipo):
		super().__init__(tipo)

	def tocar(self):
		print("Rasgueo de guitarra")
		
instrumento = Instrumento("De acordes")
instrumento.tocar()

guitarra = Guitarra("Criolla")
guitarra.tocar()