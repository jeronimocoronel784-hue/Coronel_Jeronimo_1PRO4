# 1) Factorial de un número y mostrar todos los factoriales hasta n
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial del número anterior
    return n * factorial(n - 1)

def mostrar_factoriales_hasta(n):
    for i in range(1, n + 1):
        print(f"Factorial de {i}: {factorial(i)}")

# 2) Serie de Fibonacci
def fibonacci(n):
    # Caso base: las dos primeras posiciones son 0 y 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: suma de los dos anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(hasta):
    for i in range(hasta + 1):
        print(fibonacci(i), end=" ")
    print()

# 3) Potencia (base ^ exponente)
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * base^(exponente - 1)
    return base * potencia(base, exponente - 1)

# 4) Conversión de decimal a binario (devuelve cadena)
def decimal_a_binario(n):
    # Caso base: 0 o 1 son los mismos en binario
    if n < 2:
        return str(n)
    # Caso recursivo: dividir por 2 y concatenar el resto
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    # Caso base: si tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra no coinciden, no lo es
    if palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: verificar la subcadena interna
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos de un número
def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito
    if n < 10:
        return n
    # Caso recursivo: sumar el último dígito al resultado del resto
    return (n % 10) + suma_digitos(n // 10)

# 7) Contar bloques de una pirámide
def contar_bloques(n):
    # Caso base: una sola fila tiene n = 1 bloque
    if n == 1:
        return 1
    # Caso recursivo: sumar la fila actual con las superiores
    return n + contar_bloques(n - 1)

# 8) Contar ocurrencias de un dígito dentro de un número
def contar_digito(numero, digito):
    # Caso base: si ya no quedan más cifras
    if numero == 0:
        return 0
    # Verifica si el último dígito coincide con el buscado
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplos de ejecución
if __name__ == "__main__":
    print("1) Factoriales hasta n:")
    mostrar_factoriales_hasta(5)

    print("\n2) Serie Fibonacci hasta n:")
    mostrar_serie_fibonacci(8)

    print("\n3) Potencia:")
    print("2^5 =", potencia(2, 5))

    print("\n4) Decimal a binario:")
    print("10 en binario es", decimal_a_binario(10))

    print("\n5) Palíndromo:")
    print("¿'reconocer' es palíndromo?", es_palindromo("reconocer"))

    print("\n6) Suma de dígitos:")
    print("Suma de dígitos de 305 =", suma_digitos(305))

    print("\n7) Contar bloques:")
    print("Bloques necesarios para nivel 4:", contar_bloques(4))

    print("\n8) Contar dígitos:")
    print("Cantidad de '2' en 12233421 =", contar_digito(12233421, 2))
