
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        id_str = str(producto.id)
        categoria = producto.categoria
        key = f"{categoria}_{id_str}" 
        
        if key not in self.carrito:
            self.carrito[key] = {
                "producto_id": producto.id,
                "titulo": producto.titulo,
                "precio": str(producto.precio),
                "cantidad": 1,
                "subtotal": str(producto.precio),
                "imagen": producto.imagen.url if producto.imagen else '',
                "categoria": categoria
            }
        else:
            self.carrito[key]["cantidad"] += 1
            self.carrito[key]["subtotal"] = str(round(float(self.carrito[key]["subtotal"]) + float(producto.precio), 2))
        
        self.guardar()

    def restar(self, producto):
        id_str = str(producto.id)
        categoria = producto.categoria
        key = f"{categoria}_{id_str}"
        
        if key in self.carrito:
            self.carrito[key]["cantidad"] -= 1
            self.carrito[key]["subtotal"] = str(round(float(self.carrito[key]["subtotal"]) - float(producto.precio), 2))
            if self.carrito[key]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar()

    def eliminar(self, producto):
        id_str = str(producto.id)
        categoria = producto.categoria
        key = f"{categoria}_{id_str}"
        if key in self.carrito:
            del self.carrito[key]
            self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True