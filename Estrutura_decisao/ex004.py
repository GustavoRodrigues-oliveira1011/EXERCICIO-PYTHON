letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print(f"A letra '{letra}' é uma VOGAL.")
else:
    print(f"A letra '{letra}' é uma CONSOANTE.")