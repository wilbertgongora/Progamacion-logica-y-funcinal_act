#EJEMPLO CALLBACK
'''def operar (n1,n2,funcion):
    return funcion (n1, n2)

def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

resultado = operar (5,3, resta)

print(resultado)'''

'''def saludo():
    return "¡hola!"

mi_variable = saludo ()
print(mi_variable)


def saludo2():
    return "¡que tal?!"

mi_variable2 = saludo2 ()
print(mi_variable2())
    '''

'''def elegir_operacion(operacion):
    def multiplicar(x):
        return x* 2
    def dividir (x):
        return x / 2
    if operacion == "multiplicar":
        return multiplicar
    
    else:
        return dividir
    
doble = elegir_operacion("multiplicar") # Devuelve la función multiplicar
print(doble(10))
divide2 = elegir_operacion("dividir") # Devuelve la función dividir
print(divide2(10))'''

'''    
doble = lambda x: x * 2
print (doble(5))

numeros = [1, 2, 3, 4]
dobles =list (map(lambda x: x * 2, numeros))
print (dobles)
'''

''''alumnos = [ 'wilbert', 'Miguel', 'vinicio', 'rodney', 'adrian']
saludar_alumnos = list (map(lambda nombre: 'hola' + nombre, alumnos))
print (saludar_alumnos)

def saludar (nombre):
    return 'hola' + nombre 

lista_saludos = list (map(saludar, alumnos))'''