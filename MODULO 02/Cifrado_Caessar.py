#CIFRADO CAESSAR

texto = input("Ingrese un texto a cifrar: ")

if texto == texto.upper():
    chars = "ABCDEEFGHIJKLMNOPQRSTUVWXYZ"
else:
    chars = "abcdefghijklmnopqrstuvwxyz"

desp = int(input("Ingrese el valor de desplazamiento"))

texto_cifrado = ""

for c in texto:
    if c in chars:
        texto_cifrado += chars[(chars.index(c)+desp) % len(chars)]
    else:
        texto_cifrado += c


print(f"El texto cifrado es: {texto_cifrado}")