#PILARES DE POO

class Dog:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def speak(self):
        return "woof"

dog = Dog("Bobby")
#print(dog)

"""
# Ejercicio:
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método

"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return f"{self.__marca} - {self.__modelo}"

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def mostrar_info(self):
        print(f"Vehículo: {self.__marca} {self.__modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.__ruedas = ruedas

    def __str__(self):
        return f"Marca del auto:{self.__marca}\n Modelo del auto: {self.__modelo}"

    def get_ruedas(self):
        return self.__ruedas
    
    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas
    
    def mostrar_info(self):
        print(f"Auto: {self.__marca} - {self.__modelo} - 4 ruedas")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.__ruedas = ruedas

    def __str__(self):
        return f"Marca de la moto:{self.__marca}\n Modelo de la moto: {self.__modelo}"

    def get_ruedas(self):
        return self.__ruedas
    
    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas

    def mostrar_info(self):
        print(f"Moto: {self.__marca} - {self.__modelo} - 2 ruedas")

#Llamada de la función
vehiculo_1 = Vehiculo("Toyota", "Hilux")

def imprimir_info(vehiculo):
    return vehiculo.mostrar_info()

imprimir_info(vehiculo_1)
