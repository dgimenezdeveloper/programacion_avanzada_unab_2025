class DispositivoElectronico:
    """Clase base que representa un dispositivo electrónico genérico."""
    def __init__(self, marca, modelo):
        self.marca = marca  # Propiedad pública
        self.modelo = modelo  # Propiedad pública

    def encender(self):
        """Método para encender el dispositivo."""
        return f"El dispositivo {self.marca} {self.modelo} está encendido."

    def apagar(self):
        """Método para apagar el dispositivo."""
        return f"El dispositivo {self.marca} {self.modelo} está apagado."


class Smartphone(DispositivoElectronico):
    """Clase derivada que representa un smartphone (es un dispositivo electrónico)."""
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)  # Herencia de la clase base
        self.sistema_operativo = sistema_operativo  # Propiedad adicional

    def instalar_app(self, app):
        """Método específico para instalar una aplicación."""
        return f"Instalando la aplicación {app} en el smartphone {self.marca} {self.modelo}."

    def hacer_llamada(self, numero):
        """Método específico para realizar una llamada."""
        return f"Llamando al número {numero} desde el smartphone {self.marca} {self.modelo}."



dispositivo1 = DispositivoElectronico("Sony", "X123")
dispositivo2 = DispositivoElectronico("LG", "Z456")

smartphone1 = Smartphone("Apple", "iPhone 14", "iOS")
smartphone2 = Smartphone("Samsung", "Galaxy S23", "Android")


print(dispositivo1.encender())
print(dispositivo2.apagar())

print(smartphone1.instalar_app("WhatsApp"))
print(smartphone2.hacer_llamada("+5491123456789"))

""" 

1. Encapsulamiento:
   - Las propiedades 'marca', 'modelo' y 'sistema_operativo' están encapsuladas dentro de las clases.

2. Abstracción:
   - La clase 'DispositivoElectronico' abstrae el concepto genérico de un dispositivo, mientras que 'Smartphone' agrega detalles específicos como el sistema operativo y funcionalidades adicionales.

3. Herencia:
   - La clase 'Smartphone' hereda de 'DispositivoElectronico', reutilizando sus propiedades y métodos ('encender' y 'apagar').

4. Polimorfismo:
   - Aunque 'Smartphone' hereda de 'DispositivoElectronico', puede tener métodos adicionales o redefinir métodos existentes (en este caso, no se redefinieron, pero es posible hacerlo).

"""