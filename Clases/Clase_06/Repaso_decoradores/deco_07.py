import time

def medir_tiempo(function):
	def wrapper():
		inicio = time.time()
		resultado = function()
		finalizo = time.time()
		print(f"La función tardó {finalizo - inicio} segundos en ejecutarse")
		return resultado
	return wrapper

@medir_tiempo
def tarea_larga():
	time.sleep(1)

tarea_larga()