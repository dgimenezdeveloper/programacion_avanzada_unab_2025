""" Programar en Python incluyendo constructores, atributos y métodos en base al diagrama
Usuario
------------
nombre, correo electronico, contraseña
------------
login()
logout()

********************************

usuarioGmail(Usuario)
---------------
historial_contraseñas
---------------
agregar_contraseña()
eliminar_contraseña()
historial_contraseñas()
bloqueado()

*********************************

UsuarioBasico(Usuario)
----------------------
contraseña
----------------------
login_sin_contraseñ()
bloqueado()
"""

class Usuario:
    def __init__(self, nombre, correo_electronico, contraseña):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña

    def login(self, contraseña_ingresada):
        return self.contraseña == contraseña_ingresada

    def logout(self):
        print(f"{self.nombre} ha cerrado sesión.")


class UsuarioGmail(Usuario):
    def __init__(self, nombre, correo_electronico, contraseña):
        super().__init__(nombre, correo_electronico, contraseña)
        self._historial = [contraseña]
        self._intentos_fallidos = 0

    def agregar_contraseña(self, nueva_contraseña):
        if nueva_contraseña != self.contraseña:
            self._historial.append(nueva_contraseña)
            self.contraseña = nueva_contraseña

    def eliminar_contraseña(self, contraseña):
        if contraseña in self._historial and contraseña != self.contraseña:
            self._historial.remove(contraseña)

    def historial_contraseñas(self):
        return list(self._historial)

    def bloqueado(self):
        return self._intentos_fallidos >= 3

    def login(self, contraseña_ingresada):
        if self.bloqueado():
            print("Usuario bloqueado. No puede iniciar sesión.")
            return False
        if super().login(contraseña_ingresada):
            print("Inicio de sesión exitoso.")
            self._intentos_fallidos = 0
            return True
        else:
            print("Contraseña incorrecta.")
            self._intentos_fallidos += 1
            return False


class UsuarioBasico(Usuario):
    def __init__(self, nombre, correo_electronico, contraseña):
        super().__init__(nombre, correo_electronico, contraseña)
        self._intentos_fallidos = 0

    def login_sin_contraseña(self):
        print(f"{self.nombre} ha iniciado sesión sin contraseña (modo limitado).")

    def bloqueado(self):
        return self._intentos_fallidos >= 3


