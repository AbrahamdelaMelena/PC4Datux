def sustituir(mensaje):
    llave = "abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    llave2 = "zabycxdwevfugthsijrkqlpmonñ ZABYCXDWEVFUGTHSIJRKQLPMONÑ"
   #print(llave.upper())
   #print(llave2.upper())
    mensaje_nuevo = ""

    for x in mensaje:
        for n in range(len(llave)):
            if x == llave[n]:
                mensaje_nuevo += llave2[n]
    return mensaje_nuevo


mensaje = input("Ingrese un mensaje a procesar: ")
mensaje_nuevo = sustituir(mensaje)
print(mensaje)
print(mensaje_nuevo)


