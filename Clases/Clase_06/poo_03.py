"""
### Ejercicio 3:

Define en Python dos clases:

Empleado: con atributo nombre (string) y método calcular_salario() que devuelve un valor base de 1000.
Gerente: hereda de Empleado, añade atributo bono (float) y redefine el método calcular_salario() para añadir el bono al salario base.
"""

class Empleado():
	def __init__(self, nombre, salario = 1000):
		self.__nombre = nombre
		self.__salario = salario			

	def calcular_salario(self): 
		if self.__salario != 1000:
			self.__salario = 1000
		return self.__salario
		
	def __str__(self):
		return f"Soy {self.__nombre} y cobro {self.calcular_salario()}"
	
class Gerente(Empleado):
	def __init__(self, nombre, salario, bono):
		super().__init__(nombre, salario)
		self.__bono = bono

	def calcular_salario(self):
		salario = super().calcular_salario()
		bono = salario + self.__bono
		return bono
	
#	def __str__(self):
#		return f"Gane {self.calcular_salario()}"
    

empleado = Empleado("Nico", 1000)
print(empleado.calcular_salario())
print(empleado)

gerente = Gerente("Tomas", 1000, 250)
print(gerente.calcular_salario())
print(gerente)