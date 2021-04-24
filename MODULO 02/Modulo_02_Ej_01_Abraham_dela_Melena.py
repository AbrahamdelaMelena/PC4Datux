"""
Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y permitir
el ingreso de 3 notas. Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.
"""
encabezado = ["NOMBRE", "APELLIDO", "NOTA 01", "NOTA 02", "NOTA 03"]
lista_alumno = []
contador = 0

def Alumnos():
    rpta = "si"
    contador = 0
    not1 = 11
    not2 = 11
    not3 = 11
    while rpta != "no":
        nom = (input("Ingrese el nombre del alumno: "))
        for i in nom:
            if i.isdigit():
                nom = input("El nombre no puede tener numeros, ingreselo nuevamente")
        ape = (input("Ingrese el apellido del alumno: "))
        for i in ape:
            if i.isdigit():
                ape = input("El apellido no puede tener numeros, ingreselo nuevamente")

        if not1 > 10:
            while not1 > 10:
                print("Ingrese una nota de 0 a 10")
                try:
                    not1 = int(input("Ingrese la primer nota del alumno: "))
                except ValueError:
                    print("No puede ingresar letras en este campo, vuelva a ingresar solo numeros")
                    not1 = int(input("Ingrese la primera nota del alumno entre 0 y 10"))
        if not2 > 10:
            while not2 > 10:
                print("Ingrese una nota de 0 a 10")
                try:
                    not2 = int(input("Ingrese la segunda nota del alumno: "))
                except ValueError:
                    print("No puede ingresar letras en este campo, vuelva a ingresar solo numeros")
                    not2 = int(input("Ingrese la segunda nota del alumno entre 0 y 10"))

        if not3 > 10:
            while not3 > 10:
                print("Ingrese una nota de 0 a 10")
                try:
                    not3 = int(input("Ingrese la tercera nota del alumno: "))
                except ValueError:
                    print("No puede ingresar letras en este campo, vuelva a ingresar solo numeros")
                    not3 = int(input("Ingrese la tercera nota del alumno entre 0 y 10"))

        lista_alumno.append(nom)
        lista_alumno.append(ape)
        lista_alumno.append(not1)
        lista_alumno.append(not2)
        lista_alumno.append(not3)
        lista_alumno.append("<---->")
        print(encabezado)
        print(lista_alumno)
        #No se me ocurrio otra forma de hacer que el programa continue y ya le habia dado demasiadas vueltas :´v
        not1 = 11
        not2 = 11
        not3 = 11
        contador = contador + 1

        print(f"Ha ingresado los datos de {contador} alumnos, desea continuar?")
        rpta = input("Ingrese si o no")
        if rpta == "no":
            break


Alumnos()

