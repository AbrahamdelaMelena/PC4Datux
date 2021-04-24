n = 0
m = 0 
def imprimir_linea_m(n,m):
    n = int(input("Introducir un número entre 1 y 10: "))
    m = int(input("Introducir el numero de linea que desea imprimir "))
    archivo = "tabla-" + str(n) + ".txt"
    try: 
        fichero_n = open(archivo, "r")
    except FileNotFoundError:
        print("No existe archivo asociado a la tabla ", n)
    else:
        linea = fichero_n.readlines()
        print(linea[m - 1])
imprimir_linea_m(n,m)