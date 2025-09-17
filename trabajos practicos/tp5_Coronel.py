#1 crear una lista con multiplos de 4 hasta 100
lista_multiplos = list(range(4, 101, 4))
print(lista_multiplos)

#2 crear una lista de 5 elemento y mostrar el penultimo
gustos = ["piza", "helado", "hamburguesa", "asado", "musica"]
print(gustos[-2])

#3 crear lista vacia y agregar tres palabras con append
lista_vacia = []
lista_vacia.append ("casa")
lista_vacia.append ("auto")
lista_vacia.append ("perro")
print(lista_vacia)

#4 reemplazar valores en lista animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5 expliar el codigo
# Lo que hace ese programa es crear una lsita con numeros, eliminar el mayor de ellos (el 22)
# y luego imprime por pantalla la lista sin ese numero.

#6 lista del 10 al 30 de 5 en 5 y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print(numeros[0], numeros[1])

#7 reemplazar valores en la lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ford"
autos[2] = "chevrolet"
print(autos)

#8 crear lista con dobles
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9 agregar, reemplazar y eliminar elementos
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#10 lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)