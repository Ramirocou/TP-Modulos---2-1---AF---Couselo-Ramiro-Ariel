import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").upper()
valor_genero = 10.8 if genero == "M" else 0

porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Su porcentaje de grasa corporal es: {porcentaje_grasa:.2f}%")