fecha = input("Ingrese la fecha actual con el siguiente formato 'dia,DD/MM,' \n ")

try:
    dia_semana, fecha_num = fecha.split(",")
    dia_semana = dia_semana.strip().lower()
    dia, mes = fecha_num.strip.split("/")
    dia = int(dia)
    mes = int(mes)
except:
    print("Error: formato invalido")
    exit()

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Error: fecha mal ingresada")
    exit()

if dia_semana == "lunes":
    print("Nivel Inicial")
    examenes = input("¿Hubo examenes? (si/no)").lower()
    if examenes == "si":
        aprobados = input("Ingrese la cantidad de aprobados:")
        desaprobados = input("Ingrese la cantidad de desaprobados: ")
        total = aprobados + desaprobados
        if total > 0:
            promedio = (aprobados / total) * 100 
            print(f"El porcentaje de aprobados es: {aprobados} ")
        else:
            print("No se han ingresado alumnos")
            exit()

if dia_semana == "martes":
    print("Nivel Intermedio")
    examenes = input("¿Hubo examenes? (si/no)").lower()
    if examenes == "si":
        aprobados = input("Ingrese la cantidad de aprobados:")
        desaprobados = input("Ingrese la cantidad de desaprobados: ")
        total = aprobados + desaprobados
        if total > 0:
            promedio = (aprobados / total) * 100 
            print(f"El porcentaje de aprobados es: {aprobados} ")
        else:
            print("No se han ingresado alumnos")
            exit()

if dia_semana == "miercoles":
    print("Nivel Avanzado")
    examenes = input("¿Hubo examenes? (si/no)").lower()
    if examenes == "si":
        aprobados = input("Ingrese la cantidad de aprobados:")
        desaprobados = input("Ingrese la cantidad de desaprobados: ")
        total = aprobados + desaprobados
        if total > 0:
            promedio = (aprobados / total) * 100 
            print(f"El porcentaje de aprobados es: {aprobados} ")
        else:
            print("No se han ingresado alumnos")
            exit()

if dia_semana == "jueves":
    print("Practica Hablada")
    cantidad_total = input("Ingrese la cantidad de alumnos de su curso: ")
    cantidad_asistencia = input("Ingrese la cnatidad de alumnos que asistio a su clase: ")
    promedio_alumnos = (cantidad_total / cantidad_asistencia) * 100
    if promedio_alumnos > 50:
        print("El porcentaje de alumnos que fue a su clase es mayor al 50% ")
    else:
        print("El porcentaje de alumnos fue menor al 50% ")

if dia_semana == "viernes":
    print("Ingles para viajeros")
    if mes == "1" or "7":
        print("Comienzo de nuevo ciclo ")
        cantidad_alumnos = input("Ingrese la cantidad de aumnos del nuevo ciclo: ") 
        arancel = input("Ingrese el monto a cobrar por alumno: ")
        ganancia = cantidad_alumnos * arancel
        print(f"La ganancia de este ciclo es de: {ganancia} . Con {cantidad_alumnos} alumnos y con un precio de {arancel}" )
