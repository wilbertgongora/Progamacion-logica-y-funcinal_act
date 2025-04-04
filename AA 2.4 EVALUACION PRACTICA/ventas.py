from functools import reduce

tipo_cambio = 20.53 

ventas_pesos = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

suma_ventas = reduce(lambda x, y: x + y, ventas_pesos)
promedio_ventas = suma_ventas / len(ventas_pesos)
ventas_dolares =list(map(lambda x:round(x /tipo_cambio, ventas_pesos)))
ventas_mayores =list(filter(lambda x: x > 150,ventas_dolares ))
suma_total_mayores_150 =round (reduce(lambda x, y: x + y, ventas_mayores, 0))

print("el promedio total es:", round,promedio_ventas)
print ("Las ventas de la semana en dolares es:", ventas_dolares)
print("Las ventas en dólares mayores a 150 son:", ventas_mayores)
print("La suma total de las ventas en dólares mayores a 150 es:", suma_total_mayores_150)
