valor = int(input("Digite o valor para saque (R$ 10 a R$ 600): "))

if valor < 10 or valor > 600:
    print("Valor inválido para saque.")
else:
    notas100 = valor // 100
    valor = valor % 100

    notas50 = valor // 50
    valor = valor % 50

    notas10 = valor // 10
    valor = valor % 10

    notas5 = valor // 5
    valor = valor % 5

    notas1 = valor

    print("Notas fornecidas:")
    if notas100 > 0: print(f"{notas100} nota(s) de R$ 100")
    if notas50 > 0: print(f"{notas50} nota(s) de R$ 50")
    if notas10 > 0: print(f"{notas10} nota(s) de R$ 10")
    if notas5 > 0: print(f"{notas5} nota(s) de R$ 5")
    if notas1 > 0: print(f"{notas1} nota(s) de R$ 1")