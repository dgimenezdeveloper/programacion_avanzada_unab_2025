def convertir_mayusculas(function):
	def wrapper():
		mayus = function()
		cambio = mayus.upper()
		return cambio
	return wrapper

@convertir_mayusculas
def obtener_minuscula():
	return "texto en minus"

print(obtener_minuscula())