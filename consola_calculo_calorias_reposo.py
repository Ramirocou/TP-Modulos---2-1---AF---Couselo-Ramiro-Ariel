import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en centímetros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").upper()
valor_genero = 5 if genero == "M" else -161

tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Su tasa metabólica basal es: {tmb:.2f} calorías por día")