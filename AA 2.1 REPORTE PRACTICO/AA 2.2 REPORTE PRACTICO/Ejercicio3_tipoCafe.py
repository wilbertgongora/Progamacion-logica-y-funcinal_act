def preparar_cafe_ame():
    return "cafe-americano"

def preparar_cafe_olla():
    return "cafe olla"

def ordenar_tipo_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe_ame() for _ in range(numero_tazas)]
    return tazas_cafe

def ordenar_tipo_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe_olla() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_tipo_cafe(int(input ('ingresa tu orden')))

cafe_grupo_b= ordenar_tipo_cafe(int(input ('ingresa tu orden')))

print(cafe_grupo_a)
print (cafe_grupo_b)
