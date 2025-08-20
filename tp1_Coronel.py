print("Ejercicio 1: ")
print("\n")
print("Hola Munndo! ")
print("\n")


print("Ejercicio 2: ")
print("\n")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre} ")
print("\n")


print("Ejercicio 3: ")
print("\n")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residenica = input("Ingrese sui lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residenica} ")
print("\n")

print("Ejercicio 4: ")
print("\n")
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416 
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área es: {area} ")
print(f"El perímetro es: {perimetro} ") 
print("\n")

print("Ejercicio 5: ")
print("\n")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")
print("\n")

print("Ejercicio 6: ")
print("\n")
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print("\n")


print("Ejercicio 7: ")
print("\n")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número (distinto de 0): "))
print("La suma de los numeros es:", a + b)
print("La resta de los numeros es:", a - b)
print("La multiplicacion de los numeros es:", a * b)
print("La division de los numeros es:", a / b)
print("\n")


print("Ejercicio 8: ")
print("\n")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc} ")
print("\n")


print("Ejercicio 9: ")
print("\n")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"Equivalente en Fahrenheit: {fahrenheit} ")
print("\n")

print("Ejercicio 10: ")
print("\n")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = (a + b + c) / 3
print(f"El promedio de los 3 numeros ingresados es: {promedio} ")