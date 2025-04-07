"""Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
pasa la línea en un espacio de dos dimensiones.
La clase dispondrá de los siguientes métodos:
● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
Punto, que son utilizados para inicializar los atributos.
● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique."""

import math
from ejercicio_2 import Punto


class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def __str__(self):
        return f"Linea: {self._punto_a} - {self._punto_b}"

    def mueve_derecha(self, distancia):
        self._punto_a.mover(distancia, 0)
        self._punto_b.mover(distancia, 0)

    def mueve_izquierda(self, distancia):
        self._punto_a.mover(-distancia, 0)
        self._punto_b.mover(-distancia, 0)

    def mueve_arriba(self, distancia):
        self._punto_a.mover(0, distancia)
        self._punto_b.mover(0, distancia)

    def mueve_abajo(self, distancia):
        self._punto_a.mover(0, -distancia)
        self._punto_b.mover(0, -distancia)

    # definicion de los metodos de movimiento usando set_eje_x y set_eje_y
    """ def mueve_derecha(self, distancia):
        self._punto_a.set_eje_x(self._punto_a.get_eje_x() + distancia)
        self._punto_b.set_eje_x(self._punto_b.get_eje_x() + distancia)
    
    def mueve_izquierda(self, distancia):
        self._punto_a.set_eje_x(self._punto_a.get_eje_x() - distancia)
        self._punto_b.set_eje_x(self._punto_b.get_eje_x() - distancia)
        
    def mueve_arriba(self, distancia):  
        self._punto_a.set_eje_y(self._punto_a.get_eje_y() + distancia)
        self._punto_b.set_eje_y(self._punto_b.get_eje_y() + distancia)
    
    def mueve_abajo(self, distancia):
        self._punto_a.set_eje_y(self._punto_a.get_eje_y() - distancia)
        self._punto_b.set_eje_y(self._punto_b.get_eje_y() - distancia)
 """


if __name__ == "__main__":
    p1 = Punto(1, 2)
    p2 = Punto(3, 4)
    linea = Linea(p1, p2)
    print(linea)
    linea.mueve_derecha(5)
    print(linea)
    linea.mueve_izquierda(3)
    print(linea)
    linea.mueve_arriba(2)
    print(linea)
    linea.mueve_abajo(1)
    print(linea)
