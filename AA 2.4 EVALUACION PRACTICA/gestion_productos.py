productos = ["Frijoles Refritos", "Coca Cola", 
             "Zumo de Naranja", "Café de Olla", 
             "Gorditas de Chicharrón", 
             "Huevos Motuleños"]


productos_ordenados = sorted(productos)


cadena_ordenada = ", ".join(productos_ordenados)


slugs = list(map(lambda x: x.lower().replace(" ", "-"), productos_ordenados))


print("Lista de slugs:", slugs)
print("Cadena de nombres ordenados:", cadena_ordenada)