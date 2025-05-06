""" 2. Pilares de la POO
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método.
🐀 Reflexión individual
¿Qué pilar sentís que dominás mejor? ¿Cuál te cuesta más aplicar en la práctica?
🐀 Desafío opcional
Agregá encapsulamiento con atributos privados y métodos get y set. """
# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo

# Definición de la clase hija Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas
    
    def get_puertas(self):
        return self.__puertas
    
    def set_puertas(self, puertas):
        self.__puertas = puertas
    
    def info(self):
        return f"Coche: {self.get_marca()} {self.get_modelo()}, Puertas: {self.get_puertas()}"
# Definición de la clase hija Moto

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.__cilindrada = cilindrada
    
    def get_cilindrada(self):
        return self.__cilindrada
    
    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
    
    def info(self):
        return f"Motocicleta: {self.get_marca()} {self.get_modelo()}, Cilindrada: {self.get_cilindrada()}"


def mostrar_info(vehiculo):
    print(vehiculo.info())
# Ejemplo de uso

coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "MT-07", 689)
mostrar_info(coche)
mostrar_info(moto)