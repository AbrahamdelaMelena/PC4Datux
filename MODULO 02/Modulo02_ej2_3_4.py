alumnos = {"Abraham": [5, 3, 6], "Antonio": [2, 5, 3], "Nicole": [10, 5, 3], "Hershy": [3, 1, 8]}


def evaluar_notas():
    ap = 0
    dp = 0
    for i in alumnos:
        n1 = alumnos[i][0]
        n2 = alumnos[i][1]
        n3 = alumnos[i][2]
        prom = (n1 + n2 + n3) / 3

        if prom >= 4:
            ap = ap + 1
        else:
            dp = dp + 1

        print(list(alumnos.keys())[list(alumnos.keys()).index(i)])
        print(prom)
    print(f"La cantidad de aprobados es {ap} y la de desaprobados es {dp}")


def calcular_promedio_total():
    prom_tot = 0
    prom = 0
    lista_totales = []

    for i in alumnos:
        n1 = alumnos[i][0]
        n2 = alumnos[i][1]
        n3 = alumnos[i][2]
        prom = (n1 + n2 + n3) / 3
        lista_totales.append(prom)

    for i in lista_totales:
        prom_tot = (prom_tot + i)
        prom = prom_tot/4
    print(f"El promedio total del curso es: {prom}")

def quien_mayor_menor():
    lista_totales = []
    for i in alumnos:
        n1 = alumnos[i][0]
        n2 = alumnos[i][1]
        n3 = alumnos[i][2]
        prom = (n1 + n2 + n3) / 3
        lista_totales.append(prom)
        print(int(max(lista_totales[i])))
        print(int(min(lista_totales[i])))


evaluar_notas()
calcular_promedio_total()
quien_mayor_menor()
