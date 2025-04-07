class Punto():
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
        print (f"({self.__x}, {self.__y})")

    def opuesto(self):
        return Punto(-self.__x, -self.__y)
    
#Prueba
if __name__ == "__main__":
    p1 = Punto(3,4)

    p1.impresion()
    op = p1.opuesto()
    op.impresion()
    print(p1)
