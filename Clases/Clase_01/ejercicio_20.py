class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0.")
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        # Sobrecarga del operador +
        numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __sub__(self, otra):
        # Sobrecarga del operador -
        numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __mul__(self, otra):
        # Sobrecarga del operador *
        numerador = self.numerador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def __truediv__(self, otra):
        # Sobrecarga del operador /
        if otra.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador 0.")
        numerador = self.numerador * otra.denominador
        denominador = self.denominador * otra.numerador
        return Fraccion(numerador, denominador)

    def cargar_fraccion(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0.")
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_operaciones(self, otra):
        print(f"El denominador de la primera fracción es: {self.denominador}")
        print(f"El numerador de la segunda fracción es: {otra.numerador}")
        print(f"La suma de dichas fracciones es: {self + otra}")
        print(f"La resta de dichas fracciones es: {self - otra}")
        print(f"La multiplicación de dichas fracciones es: {self * otra}")
        print(f"La división de dichas fracciones es: {self / otra}")

# Zona del programa principal
def main():
    print("Bienvenidos/as a cuentas con Fracciones")

    # Crear las fracciones
    fraccion1 = Fraccion()
    fraccion2 = Fraccion()

    # Solicitar datos para la primera fracción
    numerador1 = int(input("Ingrese el numerador de la primera fracción: "))
    denominador1 = int(input("Ingrese el denominador de la primera fracción: "))
    fraccion1.cargar_fraccion(numerador1, denominador1)

    # Solicitar datos para la segunda fracción
    numerador2 = int(input("Ingrese el numerador de la segunda fracción: "))
    denominador2 = int(input("Ingrese el denominador de la segunda fracción: "))
    fraccion2.cargar_fraccion(numerador2, denominador2)

    # Mostrar resultados de las operaciones
    fraccion1.mostrar_operaciones(fraccion2)

if __name__ == "__main__":
    main()