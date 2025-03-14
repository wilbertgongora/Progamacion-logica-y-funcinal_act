# Inicialización de los contadores de puntos para cada rama
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Imprimir el título del programa
print('=========')
print('Sombrero Seleccionador de Ramas de Sistemas Computacionales')
print('=========')

# Pregunta 1
print('\nP1) ¿Qué actividad te parece más interesante?')
print('  1) Configurar routers y switches para una red empresarial')
print('  2) Diseñar un esquema de base de datos para una aplicación')
print('  3) Programar una aplicación móvil desde cero')
print('  4) Crear un circuito electrónico para un robot')
print('  5) Modelar un personaje en 3D para un videojuego')
print('  6) Planificar el cronograma de un proyecto de software')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) ¿Qué tipo de problema te gustaría resolver?')
print('  1) Un problema de conectividad en una red local')
print('  2) Una consulta lenta en una base de datos')
print('  3) Un error en el código de una aplicación')
print('  4) Un malfuncionamiento en un dispositivo electrónico')
print('  5) Un problema de renderizado en un modelo 3D')
print('  6) Un retraso en la entrega de un proyecto')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Qué herramienta te gustaría aprender a usar?')
print('  1) Cisco Packet Tracer (simulación de redes)')
print('  2) MySQL o MongoDB (bases de datos)')
print('  3) Visual Studio Code (desarrollo de software)')
print('  4) Arduino IDE (programación de hardware)')
print('  5) Blender (modelado 3D)')
print('  6) Jira (gestión de proyectos)')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 4
print('\nP4) ¿En qué tipo de proyecto te gustaría trabajar?')
print('  1) Implementar una red segura para una empresa')
print('  2) Crear una base de datos para un sistema de ventas')
print('  3) Desarrollar una aplicación de realidad aumentada')
print('  4) Construir un robot autónomo')
print('  5) Diseñar un escenario 3D para una película')
print('  6) Liderar el lanzamiento de un nuevo software')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 5
print('\nP5) ¿Qué te parece más desafiante?')
print('  1) Asegurar una red contra ciberataques')
print('  2) Optimizar el rendimiento de una base de datos')
print('  3) Depurar un código complejo')
print('  4) Integrar hardware y software en un sistema embebido')
print('  5) Crear animaciones realistas en 3D')
print('  6) Cumplir con los plazos de un proyecto grande')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Imprimir los puntos acumulados para cada rama
print("\nResultados:")
print("Redes: ", redes)
print("Bases de Datos: ", bases_de_datos)
print("Desarrollo de Software: ", desarrollo_software)
print("Programación Hardware: ", programacion_hardware)
print("Modelado 3D: ", modelado_3d)
print("Gestión de Proyectos de Software: ", gestion_proyectos)

# Determinar y anunciar la rama con más puntos
puntos = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos de Software": gestion_proyectos
}

rama_seleccionada = max(puntos, key=puntos.get)
print(f'\n¡La rama más recomendada para ti es: {rama_seleccionada}!')