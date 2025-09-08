import random


numeros = random.sample(range(1, 51), 25)       
carton = [numeros[i:i+5] for i in range(0, 25, 5)]  
print("Bienvenido al Bingo")
print("Tu cartón es:")
for fila in carton:
    print(fila)
print()

numeros_sorteo = list(range(1, 51))
random.shuffle(numeros_sorteo)

for numero in numeros_sorteo:
    input("Presiona ENTER para sacar el siguiente número...") 
    print(f"Se sortea el número... {numero}")

    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡Lo tenés!")
    else:
        print("No está en tu cartón.")

    for fila in carton:
        print(fila)
    print()

    for fila in carton:
        if all(x == 0 for x in fila):
            print("¡Línea!\n")
            break

    todos_ceros = True
    for fila in carton:
        for valor in fila:
            if valor != 0:
                todos_ceros = False
                break
        if not todos_ceros:
            break

    if todos_ceros:
        print("¡Bingo! Tu cartón quedó en:")
        for fila in carton:
            print(fila)
        break