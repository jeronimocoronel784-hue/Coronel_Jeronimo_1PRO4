print("EJERCICIO 1: \n")
numero1 = int(input("Ingrese un numero entero: "))
print("\n")
print("\n")

print("EJERCICIO 2: \n")
numero2 = float(input("Ingrese un numero decimal: "))
print("\n")
print("\n")

print("EJERCICIO 3: \n")
suma = numero1+numero2
print("\n")
print("\n")


print("EJERCICIO 4: \n")
resta = numero1-numero2
multiplicacion = numero1*numero2
division = numero1/numero2

print(f"La suma de los dos numeros es: {suma}")
print(f"La restas de los dos numeros es: {resta}")
print(f"La multiplicacion de los dos numeros es: {multiplicacion}")
print(f"La division de los dos numeros es: {division}")
print("\n")
print("\n")

print("EJERCICIO 5: \n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("\n")

print("EJERCICIO 6: \n")
precio = float(input("Ingrese el precio del articulo: "))
print("\n")
print("\n")

print("EJERCICIO 7: \n")
print("Por ejemplo, si le quiere aplicar un 25 porciento de descuento, el valor a ingresar seria 0,25 \n")
descuento = float(input("Ingrese el valor de descuento que le quiere aplicar al producto: "))
print("\n")
print("\n")

print("EJERCICIO 8: \n")
precio_final = precio - (precio * descuento)
print(f"El precio final con el descuento aplicado es: {precio_final}")
print("\n")
print("\n")

print("EJERCICIO 9: \n")
cadena = str(input("Ingrese una frase o texto: "))
print("\n")
print("\n")

print("EJERCICIO 10: \n")
longitud = len(cadena)
print(f"La longitud de la cadena es: {longitud} caracteres")
print("\n")
print("\n")

print("EJERCICIO 11: \n")
precio = float(input("Ingrese un valor decimal para la variable precio: "))
precio_entero = int(precio)
print(f"El valor entero de la variable precio es: {precio_entero}")
print("\n")
print("\n")

print("EJERCICIO 12: \n")
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
nombre_completo = nombre + " " + apellido
print(f"Su nombre compleot es: {nombre_completo}")
print("\n")
print("\n")

print("EJERCICIO 13: \n")
edad = int(input("Ingrese su edad: "))
edad_mas_5 = edad + 5
edad_menos_10 = edad - 10 
print(f"Su edad incrementada en 5 es: {edad_mas_5}")
print(f"Su edad disminuida en 10 es: {edad_menos_10}")
print("\n")
print("\n")

print("EJERCICIO 14: \n")
altura = float(input("Ingrese la altura en metros (Ejemplo 1.90): "))
altura_cm = altura * 180
resultado = (altura *4) / 3
print(f"Su altura en centimetros es: {altura_cm} cm")
print(f"Su altura multiplicada por 4 y luego dividida en 3 es: {resultado}")
print("\n")
print("\n")

print("EJERCICIO 15: \n")
nombre_mayus = str(input("Ingrese su nombre completo en mayusculas: "))
nombre_minus = nombre_mayus.lower()
print(f"Su nombre en minusculas es: {nombre_minus}")
print("\n")
print("\n")

print("EJERCICIO 16: \n")
nombre_mayuscula = nombre_mayus.capitalize()
print(f"Su nombre con solo la primera letra en mayuscula es: {nombre_mayuscula}")
print("\n")
print("\n")