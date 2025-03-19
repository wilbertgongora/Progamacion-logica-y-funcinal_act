def duplicar_almacenamiento(espacio):
    return espacio * 2  

def reducir_almacenamiento(espacio):
    return espacio / 2

def elegir_operacion(operacion):
    if operacion == "duplicar":
        return duplicar_almacenamiento  
    else:
        return reducir_almacenamiento


ajustar = elegir_operacion("duplicar") 
print(f"Capacidad luego de duplicar: {ajustar(500)} GB")  

ajustar = elegir_operacion("reducir")  # Elegimos reducir
print(f"Capacidad luego de reducir: {ajustar(500)} GB")  
