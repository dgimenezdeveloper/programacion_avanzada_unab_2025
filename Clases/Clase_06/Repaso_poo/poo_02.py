"""
### Ejercicio 2:

Define en Python dos clases:

Figura: con atributo color (string) y método area() que devuelve 0 (ya que es una figura genérica).
Cuadrado: hereda de Figura, añade atributo lado (float) y redefine el método area() para calcular y devolver el área del cuadrado.
"""

class Figura():
	def __init__(self, color):
		self.__color = color

	def area(self):
		return 0

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado	
        
    def area(self):
        resultado = self.__lado * self.__lado
        return resultado
		
cuadrado = Cuadrado("Rojo", 4)
area = cuadrado.area()
print(area)