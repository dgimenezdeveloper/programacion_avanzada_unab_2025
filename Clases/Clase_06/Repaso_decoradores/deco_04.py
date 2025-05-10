def agregar_exclamacion(function):
	def wrapper():
		a = function()
		return a+"!"
	return wrapper

@agregar_exclamacion
def obtener_saludo():
	return "Buenos dias"

print(obtener_saludo())