import math


class Punto:
    """Clase que representa un punto en el plano cartesiano."""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def get_eje_x(self):
        return self.__x

    def get_eje_y(self):
        return self.__y

    def set_eje_x(self, x):
        self.__x = x

    def set_eje_y(self, y):
        self.__y = y

    def impresion(self):
        print(f"({self.__x}, {self.__y})")

    def opuesto(self):
        """Devuelve un nuevo punto que es el opuesto del actual."""
        return Punto(-self.__x, -self.__y)

    def distancia(self, p2):
        """Devuelve la distancia entre el punto actual y otro punto."""
        return math.sqrt((self.__x - p2.__x) ** 2 + (self.__y - p2.__y) ** 2)

    def mover(self, dx, dy):
        """Desplaza el punto en el plano cartesiano."""
        self.__x += dx
        self.__y += dy


###### Programa principal ######
if __name__ == "__main__":
    p1 = Punto(4, 2)
    p2 = Punto(2, 2)

    p1.impresion()
    op = p1.opuesto()
    op.impresion()
    print(p1)

    resultado = p1.distancia(p2)
    print(resultado)
