alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese el corrimiento: "))
for i in range (5):
    mensaje = input(f"Ingrese el mensaje a mandar {i+1}: ")
    encriptado = ""
    for letra in mensaje.lower():
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_encriptado = (indice + corrimiento)% 27
            encriptado = encriptado + alfabeto[indice_encriptado]
        else: 
            encriptado = encriptado + letra
    print(f"Mensaje encripado {i + 1}: {encriptado}")