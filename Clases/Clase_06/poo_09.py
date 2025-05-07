"""
Ejercicio 9:
Define en Python dos clases:

CuentaBancaria: con atributo saldo (float) y método depositar(cantidad) que incrementa el saldo. 
CuentaCorriente: hereda de CuentaBancaria y añade un atributo limite_sobregiro (float).	
"""

class CuentaBancaria():
	def __init__(self, saldo, cantidad):
		self.__saldo = saldo
		self.__cantidad = cantidad

	def depositar(self):
		saldo = self.__saldo + self.__cantidad
		print(saldo)

class CuentaCorriente(CuentaBancaria):
	def __init__(self, saldo, cantidad, limite_sobregiro):
		super().__init__(saldo, cantidad)
		self.__limite_sobregiro = limite_sobregiro
		
cuenta_1 = CuentaBancaria(1000, 500)
cuenta_1.depositar()