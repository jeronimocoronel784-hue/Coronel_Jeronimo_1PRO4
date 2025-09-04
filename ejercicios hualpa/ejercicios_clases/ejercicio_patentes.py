
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]

cantidad = int(input("Ingrese la cantidad de patentes a generar: "))
generadas = 0

for i in range(len(abecedario)):
    for j in range(len(abecedario)):
        for k in range(len(abecedario)):
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        print(f"{abecedario[i]}{abecedario[j]}{abecedario[k]} {a}{b}{c}")
                        generadas == generadas+1
                        if generadas >= cantidad:
                            break
                    if generadas >= cantidad: break
                if generadas >= cantidad: break
            if generadas >= cantidad: break
        if generadas >= cantidad: break
    if generadas >= cantidad: break

