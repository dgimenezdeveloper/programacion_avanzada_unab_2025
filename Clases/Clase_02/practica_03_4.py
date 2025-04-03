class DispositivoElectronico:
    """Clase base que representa un dispositivo electrónico genérico."""
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    def encender(self):
        """Método para encender el dispositivo."""
        return f"El dispositivo {self.__marca} {self.__modelo} está encendido."

    def apagar(self):
        """Método para apagar el dispositivo."""
        return f"El dispositivo {self.__marca} {self.__modelo} está apagado."


class Smartphone(DispositivoElectronico):
    """Clase derivada que representa un smartphone (es un dispositivo electrónico)."""
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)  # Herencia de la clase base
        self.__sistema_operativo = sistema_operativo  # Atributo privado

    def instalar_app(self, app):
        """Método específico para instalar una aplicación."""
        return f"Instalando la aplicación {app} en el smartphone."

    def hacer_llamada(self, numero):
        """Método específico para realizar una llamada."""
        return f"Llamando al número {numero} desde el smartphone."


dispositivo1 = DispositivoElectronico("Sony", "X123")
dispositivo2 = DispositivoElectronico("LG", "Z456")

smartphone1 = Smartphone("Apple", "iPhone 14", "iOS")
smartphone2 = Smartphone("Samsung", "Galaxy S23", "Android")

print(dispositivo1.encender())
print(dispositivo2.apagar())

print(smartphone1.instalar_app("WhatsApp"))
print(smartphone2.hacer_llamada("+5491123456789"))

# Usando dir para inspeccionar un objeto
print(dir(smartphone1))