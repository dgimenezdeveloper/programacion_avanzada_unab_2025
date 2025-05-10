def mostrar_ejecucion(function):
	def nuevo_saludar():
		print("La función fue ejecutada")
		function()
	return nuevo_saludar()

@mostrar_ejecucion
def saludar_simple():
	print("Hola")

saludar_simple()

