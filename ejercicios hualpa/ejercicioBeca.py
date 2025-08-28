print(" Sistema de Becas Estudiantiles ")

# 1. Nombre y apellido
nombre = input("Ingrese su nombre y apellido: ")

# 2. Edad (validada)
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break
        else:
            print(" La edad debe ser un número positivo.")
    except ValueError:
        print(" Ingrese un número válido para la edad.")

# 3. Promedio general (validado entre 0 y 10)
while True:
    try:
        promedio = float(input("Ingrese su promedio general (0-10): "))
        if 0 <= promedio <= 10:
            break
        else:
            print(" El promedio debe estar entre 0 y 10.")
    except ValueError:
        print(" Ingrese un número válido para el promedio.")

# 4. Ingresos familiares (solo números)
while True:
    try:
        ingresos = float(input("Ingrese los ingresos familiares mensuales: $"))
        if ingresos >= 0:
            break
        else:
            print("Los ingresos no pueden ser negativos.")
    except ValueError:
        print(" Ingrese un valor numérico válido para los ingresos.")

# Evaluación de la beca
if promedio < 6:
    resultado = "Rechazado"
else:
    if ingresos < 300000:
        resultado = "Beca completa"
    elif 300000 <= ingresos <= 600000:
        resultado = "Media beca"
    else:
        resultado = "Rechazado"

# Salida final
print("\n", nombre, f", {edad} años")
print(f"Promedio: {promedio}")
print(f"Ingresos: ${int(ingresos)}")
print("Resultado:", resultado)
