def aplicar_funcion(maestros, funcion):
    return [funcion(m) for m in maestros]

maestros = ["paloma", "noemi", "placido"]
print(aplicar_funcion(maestros, str.upper))