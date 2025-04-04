def cuadradosLista(arreglo):
    # Filtrar primero los enteros positivos
    enteros_positivos = filter(lambda x: x > 0 and x == int(x), arreglo)
    # Calcular sus cuadrados
    cuadrados = map(lambda x: x ** 2, enteros_positivos)
    return list(cuadrados)

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)  # Salida esperada: [25, 9]