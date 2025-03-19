# Listas de servidores y sus estados
servidores = ['Servidor Web', 'Servidor de Base de Datos', 'Servidor de Correo', 'Servidor de Archivos', 'Servidores Wilbert']
estados = [True, False, True, False, True]

# Filtrar servidores en línea usando filter y lambda
servidores_en_linea = list(filter(lambda x: x[1], zip(servidores, estados)))

# Mostrar servidores en línea
print("Servidores en línea:")
for servidor in servidores_en_linea:
    print(servidor[0])