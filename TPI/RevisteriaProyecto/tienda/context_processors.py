from .carrito import Carrito

def importe_total(request):
    """ Calcula el importe total del carrito de compras."""
    carrito = Carrito(request)
    total = 0
    for key, value in carrito.carrito.items():
        total += float(value.get("subtotal", 0))
    return {"importe_total_carrito": total}