def calc_soluc():
    
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))
    c = float(input("Escriba el valor del coeficiente c: "))

    d = b * b - 4 * a * c
    if a == b == c == 0:
        print("Todos los números son solución.")
    elif a == b == 0:
        print("La ecuación no tiene solución.")
    elif a == 0:
        print(f"La ecuación tiene una solución: {- c / b}")
    elif d < 0:
        print("La ecuación no tiene solución real.")
    elif d == 0:
        print(f"La ecuación tiene una solución: {- b / (2 * a)}")
    else:
        print(
            f"La ecuación tiene dos soluciones: {(-b - d ** 0.5) / (2 * a)} y {(-b + d ** 0.5) / (2 * a)}"
        )


calc_soluc()