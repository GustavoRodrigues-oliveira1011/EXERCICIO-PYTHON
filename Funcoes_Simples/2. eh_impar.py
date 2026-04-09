def eh_Impar(numero):
    return numero % 2 !=0

numero = int(input("Digite um número: "))

if eh_Impar(numero):
    print(f"O número {numero} é ímpar")
else:
    print(f"O número {numero} é par")