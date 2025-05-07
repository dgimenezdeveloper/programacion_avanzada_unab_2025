"""
Ejercicio 8:
Define en Python dos clases:

Forma: con método dibujar() que imprime "Dibujando una forma genérica". 
Circulo: hereda de Forma, añade atributo radio (float) y 
	redefine el método dibujar() para imprimir "Dibujando un círculo de radio ".
"""

class Forma():
	
	def dibujar(self):
		print("Dibujando una forma genérica")		

class Circulo(Forma):
	def __init__(self, radio):
		self.__radio = radio

	def dibujar(self):
		print(f"Dibujando un circulo de radio: {self.__radio}")
		
forma_1 = Forma()
forma_1.dibujar()

circulo_1 = Circulo(20)
circulo_1.dibujar()