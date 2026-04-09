n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in "ABC":
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print("-" * 20)
print(f"Notas: {n1} e {n2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")