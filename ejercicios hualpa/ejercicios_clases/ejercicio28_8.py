nombre_completo = input("Ingrese su nombre y apellido: ")
edad = input("Ingrese su edad en numeros: ")
promedio = int(input("Ingrese su promedio: "))
ingresos_fam = int(input("Ingrese sus ingresos familiares mensuales: "))
beca = bool
resultado = str
if promedio < 6 :
    resultado = "Beca rechazada"
    print(f"Para poder acceder a la beca necesita promedio mayor a 6. {resultado}")
elif promedio > 6 and ingresos_fam < 300000 :
        resultado = "Beca completa"
        beca = True
elif promedio > 6 and  ingresos_fam >= 300000 and ingresos_fam <= 600000 : 
        resultado = "Media beca"
        beca = True
else :
    resultado = "Beca rechazada"
    beca = False
    print(f"Para acceder a la beca los ingresos familiares deben rondar entre $300000 y $600000." )
print("\n")

print(f"{nombre_completo} , {edad} años ")
print(f"Promedio: {promedio}")
if resultado == "Media beca" :
    print(f"Resultado: {resultado} ")
elif resultado == "Beca completa" :
    print(f"Resultado: {resultado} ")
else :
    print("Beca rechazada")