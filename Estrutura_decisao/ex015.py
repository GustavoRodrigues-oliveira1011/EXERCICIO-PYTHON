lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero (3 lados iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles (2 lados iguais)")
    else:
        print("Triângulo Escaleno (3 lados diferentes)")
else:
    print("Os valores não podem formar um triângulo.")