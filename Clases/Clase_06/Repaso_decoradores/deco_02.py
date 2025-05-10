def envolver_parentesis(function):
	def texto_nuevo():
		a = function()
		return f"({a})"
	return texto_nuevo

@envolver_parentesis
def obtener_texto():
	return "un texto"

print(obtener_texto())
