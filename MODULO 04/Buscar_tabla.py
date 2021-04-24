n = 0
def buscar_fichero(n):  
    n = int(input("Introduce un número entero entre 1 y 10: "))
    archivo = "tabla-" + str(n) + ".txt"
    try: 
        f = open(archivo, "r")
    except FileNotFoundError:
        print("No hay un archivo con la tabla", n)
    else:
        print(f.read())

buscar_fichero(n)