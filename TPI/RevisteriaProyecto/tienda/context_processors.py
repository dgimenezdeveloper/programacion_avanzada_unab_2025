from .carrito import Carrito

def importe_total(request):
    carrito = Carrito(request)
    total = 0
    for key, value in request.session.get("carrito", {}).items():
        total += float(value.get("subtotal", 0))
    return {"importe_total_carrito": total}