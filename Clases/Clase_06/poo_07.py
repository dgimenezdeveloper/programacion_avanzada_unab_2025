"""
Ejercicio 7:
Define en Python dos clases:

Producto: con atributo nombre (string) y método obtener_precio() que devuelve 0. 
ProductoConDescuento: hereda de Producto, añade atributo descuento (float) y 
redefine obtener_precio() para aplicar el descuento a un precio base (por ejemplo, 100).
"""

class Producto():
	def __init__(self, nombre, precio = 0):
		self.__nombre = nombre
		self.__precio = precio

	def obtener_precio(self):
		if self.__precio != 0:
			self.__precio = 0
		return self.__precio
		

class ProductoConDescuento(Producto):
	def __init__(self, nombre, precio, descuento):	
		super().__init__(nombre, precio)
		self.__descuento = descuento

	def obtener_precio(self):
		precio = (self._Producto__precio * self.__descuento) / 100		
		return self._Producto__precio - precio
	

producto_1 = Producto("Alfajor", 100)		
print(producto_1.obtener_precio())

producto_desc_1 = ProductoConDescuento("Alfajor_", 100, 20)
print(producto_desc_1.obtener_precio())