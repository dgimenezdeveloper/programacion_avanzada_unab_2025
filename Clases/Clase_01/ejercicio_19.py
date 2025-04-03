""" Ejercicio 19: Implementar el Ejercicio 14 utilizando clases con jerarquía y herencia. """

class ConversorMoneda:
    """Clase base para convertir montos en pesos argentinos a diferentes monedas."""
    
    def __init__(self, monto_en_pesos):
        self.monto_en_pesos = monto_en_pesos

    def convertir(self):
        """Método genérico que debe ser implementado por las subclases."""
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


class ConversorDolar(ConversorMoneda):
    """Clase para convertir pesos argentinos a dólares."""
    
    def convertir(self):
        tasa_cambio_dolar = 0.0022
        return self.monto_en_pesos * tasa_cambio_dolar


class ConversorEuro(ConversorMoneda):
    """Clase para convertir pesos argentinos a euros."""
    
    def convertir(self):
        tasa_cambio_euro = 0.00084
        return self.monto_en_pesos * tasa_cambio_euro


class ConversorReal(ConversorMoneda):
    """Clase para convertir pesos argentinos a reales brasileños."""
    
    def convertir(self):
        tasa_cambio_real = 0.0055
        return self.monto_en_pesos * tasa_cambio_real


if __name__ == "__main__":
    monto = 10000  # Monto en pesos argentinos

    conversor_dolar = ConversorDolar(monto)
    conversor_euro = ConversorEuro(monto)
    conversor_real = ConversorReal(monto)

    print(f"{monto} pesos son {conversor_dolar.convertir():.2f} dólares.")
    print(f"{monto} pesos son {conversor_euro.convertir():.2f} euros.")
    print(f"{monto} pesos son {conversor_real.convertir():.2f} reales.")