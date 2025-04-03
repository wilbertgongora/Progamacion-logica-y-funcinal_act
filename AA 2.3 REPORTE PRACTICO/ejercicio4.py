def agregar_asignatura(lista):
    asig_nueva = input("Ingrese una nueva asignatura nueva o 'no' para salir: " )
    if asig_nueva == "no":
        return lista
    return agregar_asignatura(lista + [asig_nueva])
asignatura= ["graficacion", "redes", "inteligencia artificial"]

print(agregar_asignatura(asignatura))