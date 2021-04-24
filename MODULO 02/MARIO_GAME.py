h = int(input("ingrese la altura de la media piramide"))

while (h < 0 or h > 8):
    print("ingresar un valor no mayor a 8")
    h = int(input("ingrese la altura de la media piramide: "))
print(f"altura : {h}")
for i in range(h):
    print(" " * (h - i) + "#" * (i + 1))
