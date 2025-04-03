asignaturas_viii =["Programacion web"]
#b =asignaturas_viii + ["Base de datos"]

#print(asignaturas_viii, b)

def agregar_asignatura(lista,asignatura):
    return lista + [asignatura]

c=agregar_asignatura (asignaturas_viii, input('ingrese la asigatura:'))
print (agregar_asignatura(asignaturas_viii, c))