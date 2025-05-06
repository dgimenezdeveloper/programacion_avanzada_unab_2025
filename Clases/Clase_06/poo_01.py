"""
Define en Python dos clases:

Animal: con atributo nombre (string) y método emitir_sonido() que imprime "Sonido genérico de animal".
Perro: hereda de Animal y redefine el método emitir_sonido() para imprimir "¡Guau!".
"""

class Animal():
	def __init__(self, nombre):
		self.__nombre = nombre

	def emitir_sonido(self):
		print("Sonido genérico de animal")

class Perro(Animal):
	def emitir_sonido(self):
		print("!Guau¡")
		
animal = Animal("Lola")
animal.emitir_sonido() 
       
perro = Perro("Fatiga")
perro.emitir_sonido()