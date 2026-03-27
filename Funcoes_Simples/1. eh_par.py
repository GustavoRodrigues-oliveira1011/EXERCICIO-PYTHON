def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número: "))

if eh_par(numero):
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")