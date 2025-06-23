import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en centímeros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").upper()
valor_genero = 5 if genero == "M" else -161

print("Nivel de actividad física:")
print("1. Poco o ningún ejercicio")
print("2. Ejercicio ligero (1-3 días/semana)")
print("3. Ejercicio moderado (3-5 días/semana)")
print("4. Deportista (6-7 días/semana)")
print("5. Atleta (entrenamientos mañana y tarde)")
op = int(input("Seleccione una opción (1-5): "))
actividad = [1.2, 1.375, 1.55, 1.725, 1.9][op - 1]

tmb_act = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, actividad)
print(f"Calorías diarias estimadas con su actividad física: {tmb_act:.2f}")