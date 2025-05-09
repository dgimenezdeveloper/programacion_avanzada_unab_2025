"""
### Ejercicio 6:

Define en Python dos clases:

Dispositivo: con atributo nombre (string) y método encender() que imprime "<nombre> encendido".
Telefono: hereda de Dispositivo, añade atributo numero (string) y 
redefine el método encender() para imprimir "<nombre> (Número: &lt;numero>) encendido".
"""

class Dispositivo():
	def __init__(self, nombre):
		self.__nombre = nombre

	def encender(self):
		print(f"{self.__nombre} encendido")

class Telefono(Dispositivo):
	def __init__(self, nombre, numero):
		super().__init__(nombre)
		self.__numero = numero

	def encender(self):
		print(f"{self._Dispositivo__nombre}, Número: {self.__numero} encendido")
		
# Ejemplo de uso
dispositivo = Dispositivo("PC")
dispositivo.encender()

telefono = Telefono("Celular", "123456789")
telefono.encender()