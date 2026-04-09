palavra = input("Digite uma palavra ou frase: ").upper()

palavra_limpa = palavra.replace(" ", "")

palavra_invertida = palavra_limpa[::-1]

if palavra_limpa == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")