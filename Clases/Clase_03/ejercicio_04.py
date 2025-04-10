class Persona():
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return self.__nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

class Cancion():
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def __str__(self):
        return f"{self.__titulo} de {self.__autor}"

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

#Prueba
if __name__ == "__main__":
    persona_1 = Persona("QUEEN")
    print(persona_1)
    cancion_1 = Cancion("Bohemian Rhapsody", persona_1)
    print(cancion_1)
    print(cancion_1.get_autor())
    #persona_1.set_nombre("Dra Queen")
    cancion_1.set_autor("Dra Queen")#Es buena practica hacer esto?
    print(cancion_1)