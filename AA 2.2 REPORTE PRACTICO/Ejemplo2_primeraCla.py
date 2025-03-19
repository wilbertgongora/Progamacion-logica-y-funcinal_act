def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento)

def calcular_total(func, precio, descuento):
    return func(precio, descuento)

precio_colegio = 100
descuento = 0.20
print("Precio con descuento de la carrrera es:", calcular_total(aplicar_descuento, precio_colegio, descuento))