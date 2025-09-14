# ===============================
# EJERCICIO 1
# Imprimir números del 0 al 100
# ===============================
for i in range(101):
    print(i)



# EJERCICIO 2
# Contar los dígitos de un número
# ===============================
num = int(input("Ejercicio 2 - Ingresa un número entero: "))
contador = 0

if num == 0:
    contador = 1
else:
    while num != 0:
        contador += 1
        num //= 10

print("Cantidad de dígitos:", contador)


# ===============================
# EJERCICIO 3
# Suma entre dos valores (excluyendo extremos)
# ===============================
a = int(input("Ejercicio 3 - Ingresa el primer número: "))
b = int(input("Ejercicio 3 - Ingresa el segundo número: "))

suma = 0
for i in range(a + 1, b):
    suma += i

print("La suma es:", suma)


# ===============================
# EJERCICIO 4
# Sumar números hasta que se ingrese 0
# ===============================
suma = 0
while True:
    num = int(input("Ejercicio 4 - Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)


# ===============================
# EJERCICIO 5
# Juego de adivinar un número
# ===============================
import random

numero = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Ejercicio 5 - Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero:
        adivinado = True

print("¡Correcto! Lo lograste en", intentos, "intentos.")


# ===============================
# EJERCICIO 6
# Números pares del 100 al 0 en orden decreciente
# ===============================
for i in range(100, -1, -2):
    print(i)


# ===============================
# EJERCICIO 7
# Suma desde 0 hasta un número dado
# ===============================
n = int(input("Ejercicio 7 - Ingresa un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("La suma es:", suma)


# ===============================
# EJERCICIO 8
# Contar pares, impares, negativos y positivos
# ===============================
cantidad = 100  # cambiar este valor para probar con menos números
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input("Ejercicio 8 - Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)


# ===============================
# EJERCICIO 9
# Calcular la media de 100 números
# ===============================
cantidad = 100  # cambiar este valor para probar con menos números
suma = 0

for i in range(cantidad):
    num = int(input("Ejercicio 9 - Ingresa un número: "))
    suma += num

media = suma / cantidad
print("La media es:", media)


# ===============================
# EJERCICIO 10
# Invertir los dígitos de un número
# ===============================
num = int(input("Ejercicio 10 - Ingresa un número: "))
invertido = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10

print("Número invertido:", invertido)
