def saludar(function):
	def wrapper():
		print("¡Hola!")
		return function()
	return wrapper

@saludar
def presentarse():
	print("Soy una función")

presentarse()