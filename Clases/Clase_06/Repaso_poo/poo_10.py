"""
Ejercicio 10:
Define en Python dos clases:

Electrodomestico: con atributo marca (string) y método informar() que devuelve "Electrodoméstico marca ". 
Lavadora: hereda de Electrodomestico, añade atributo capacidad (float) y 
	redefine informar() para devolver "Lavadora marca , capacidad: kg".

"""

class Electrodomestico():
    def __init__(self, marca):
        self.__marca = marca

    def informar(self):
        return f"Marca del electrdomestico: {self.__marca}"

class Lavadora(Electrodomestico):
	def __init__(self, marca, capacidad):
		super().__init__(marca)
		self.__capacidad = capacidad

	def informar(self):
		return f"Marca de la Lavadora: {self._Electrodomestico__marca} \nCapacidad: {self.__capacidad} kg"

electro_d_1 = Electrodomestico("Hitachi")

lavadora_1 = Lavadora("Sony", 20)  
print(lavadora_1.informar())
