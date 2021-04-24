n = 0
def crear_ficheros(n):
    n = int(input("Introduce un número entre 1 y 10: "))

    archivo = "tabla-" + str(n) + ".txt"

    fichero_n = open(archivo, "w")

    for i in range(1, 13):
        fichero_n.write(str(n) + " x " + str(i) + " = " + str(n * i) + "\n")

    fichero_n.close()

crear_ficheros(n)