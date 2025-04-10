"""
Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre 
cada  libro:  título,  autor  (usa  la  clase  Persona),  ISBN,  páginas,  edición,  editorial  ,  lugar 
(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes 
servicios:  getters  y  setters,  método  para  leer  la  información  y  método  para  mostrar  la 
información.
"""
from ejercicio_04 import Persona

class Libro():
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__paginas = paginas
        self.__edicion = edicion
        self.__editorial = editorial
        self.__lugar = lugar
        self.__fecha_edicion = fecha_edicion
    
    def __str__(self):
        return f"""\tTitulo: {self.__titulo} 
\tAutor: {self.__autor}
\tISBN: {self.__isbn}
\t{self.__lugar}
\t{self.__fecha_edicion}
\t{self.__paginas} paginas"""

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo_nuevo):
        self.__titulo = titulo_nuevo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor_nuevo):
        self.__autor = autor_nuevo

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn_nuevo):
        self.__isbn = isbn_nuevo
   
    def get_paginas(self):
        return self.__paginas
   
    def set_paginas(self, paginas_nuevas):
        self.__paginas = paginas_nuevas

    def get_edicion(self):
        return self.__edicion
    
    def set_edicion(self, edicion_nueva):
        self.__edicion = edicion_nueva

    def get_editorial(self):
        return self.__editorial
    
    def set_editorial(self, editorial_nueva):
        self.__editorial = editorial_nueva

    def get_lugar(self):
        return self.__lugar
    
    def set_lugar(self, lugar_nuevo):
        self.__lugar = lugar_nuevo

    def get_fecha_edicion(self):
        return self.__fecha_edicion
    
    def set_fecha_edicion(self, fecha_edicion_nuevo):
        self.__fecha_edicion = fecha_edicion_nuevo

#Prueba
if __name__ == "__main__":
    autor = Persona("Jorge Luis Borges")
    libro_1 = Libro("Cuentos de cumpleaños", autor, "0-13-031997-X", 854, "Primera Edicion", "Lumen", "Buenos Aires, Argentina", "10/04/2015")
    print(libro_1)