def validacion_tarjetas(numero):
    tarjeta = ""
    par = 0
    impar = 0
    x = ""

    if not numero.isdigit():
        return 1, ""
    if len(numero) < 14 or len(numero) > 19:
        return 2, ""
    for c in range(0, len(numero), 2):
        x = str(int(numero[c]) * 2)
        if len(x) == 2:
            par += (int(x[0]) + int(x[1]))
        else:
            par += int(x)
    for c in range(1, len(numero), 2):
        impar += int(numero[c])
    if (par + impar) % 10 != 0:

        return 3, " "
    if numero[0:2] > "49" or numero[0:2] < "56":
        tarjeta = "MasterCard"
    if numero[0:2] == "34" or numero[0:2] == "37":
        tarjeta = "AMEX"
    if numero[0] == "4":
        tarjeta = "VISA"
    return 4, tarjeta


msg = (0, "")
while msg[0] != 4:

    msg = validacion_tarjetas(input("Ingrese el numero de una tarjeta: "))

    if msg[0] == 1:
        print("solo ingresar numeros")
    if msg[0] == 2:
        print("la cantidad de caracteres debe estar entre 13 y 19 como maximo")
    if msg[0] == 3:
        print("NUMERO INVALIDO")



print("NUMERO INGRESADO VALIDO")

print("Tipo de tarjeta: " + msg[1])
