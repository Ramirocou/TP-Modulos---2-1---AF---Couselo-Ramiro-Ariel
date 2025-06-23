def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    imc = calcular_IMC(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_min = tmb * 0.80
    calorias_max = tmb * 0.85
    return f"Para adelgazar es recomendado que consumas entre: {calorias_min:.2f} y {calorias_max:.2f} calorías al día."