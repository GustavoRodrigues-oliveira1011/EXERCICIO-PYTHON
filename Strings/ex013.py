palavra_orig = input("Digite a palavra original: ").upper()

meio = len(palavra_orig) // 2

palavra_baguncada = palavra_orig[meio:] + palavra_orig[:meio][::-1]

print(f"A palavra embaralhada é: {palavra_baguncada}")

chute = input("Qual é a palavra original? ").upper()

if chute == palavra_orig:
    print("Boa! Você acertou.")
else:
    print(f"Errou! A palavra era {palavra_orig}")