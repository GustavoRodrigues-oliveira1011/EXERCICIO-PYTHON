a = float(input("Valor de a: "))

if a == 0:
    print("A equação não é de segundo grau.")
else:
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"Raiz única: {raiz}")
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Duas raízes: {raiz1:.2f} e {raiz2:.2f}")
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}") 