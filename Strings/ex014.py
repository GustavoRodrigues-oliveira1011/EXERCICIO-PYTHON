texto = input("Digite uma frase: ").upper()

texto = texto.replace("A", "4")
texto = texto.replace("E", "3")
texto = texto.replace("I", "1")
texto = texto.replace("O", "0")
texto = texto.replace("T", "7")
texto = texto.replace("S", "5")

print(f"Texto em Leet Speak: {texto}")