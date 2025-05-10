def envolver_en_html(tag='div'):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            res = funcion(*args, **kwargs)
            return f'<{tag}> {res} </{tag}>'
        return wrapper
    return decorador

@envolver_en_html()
def obtener_nombre():
    return "Juan"


print(obtener_nombre())
