""" Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real.
Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión
respectiva. """

def convertir_a_dolar(monto_en_pesos):
    """Convierte un monto en pesos argentinos a dólares."""
    tasa_cambio_dolar = 0.0022
    return monto_en_pesos * tasa_cambio_dolar

def convertir_a_euro(monto_en_pesos):
    """Convierte un monto en pesos argentinos a euros."""
    tasa_cambio_euro = 0.00084
    return monto_en_pesos * tasa_cambio_euro

def convertir_a_real(monto_en_pesos):
    """Convierte un monto en pesos argentinos a reales brasileños."""
    tasa_cambio_real = 0.0055
    return monto_en_pesos * tasa_cambio_real

# Ejemplo de uso
if __name__ == "__main__":
    monto = 10000  # Monto en pesos argentinos
    print(f"{monto} pesos son {convertir_a_dolar(monto):.2f} dólares.")
    print(f"{monto} pesos son {convertir_a_euro(monto):.2f} euros.")
    print(f"{monto} pesos son {convertir_a_real(monto):.2f} reales.")