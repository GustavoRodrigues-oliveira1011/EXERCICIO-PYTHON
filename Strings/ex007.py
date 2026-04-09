frase = input("Digite uma frase: ").lower()


espacos = frase.count(" ")

# Contamos cada vogal individualmente
vogais_a = frase.count("a")
vogais_e = frase.count("e")
vogais_i = frase.count("i")
vogais_o = frase.count("o")
vogais_u = frase.count("u")

total_vogais = vogais_a + vogais_e + vogais_i + vogais_o + vogais_u

print(f"Espaços em branco: {espacos}")
print(f"Total de vogais: {total_vogais}")