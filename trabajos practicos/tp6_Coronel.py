def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Ejercicio 2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))


# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido, ", tengo", edad, "años y vivo en", residencia)

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4
def calcular_area_circulo(radio):
    return 3.1416 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

radio = float(input("Ingresa el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))


# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa los segundos: "))
print("Equivalen a", segundos_a_horas(segundos), "horas")


# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

num = int(input("Ingresa un número para ver su tabla: "))
tabla_multiplicar(num)


# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
resultados = operaciones_basicas(a, b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])


# Ejercicio 8 
def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))
print("Tu IMC es:", round(calcular_imc(peso, altura), 2))


#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))


# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
print("El promedio es:", calcular_promedio(a, b, c))
