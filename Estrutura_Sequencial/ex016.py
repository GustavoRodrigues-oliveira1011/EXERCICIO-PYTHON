area = float(input("Digite a área em m²: "))

litros = area / 3
capacidade_lata = 18

quantidade_latas = litros // capacidade_lata
if litros % capacidade_lata > 0:
    quantidade_latas = quantidade_latas + 1

custo_total = quantidade_latas * 80

print(f"Precisa de {quantidade_latas} latas.")
print(f"Total: R$ {custo_total:.2f}")

