kg_morango = float(input("Kg de morangos: "))
kg_maca = float(input("Kg de maçãs: "))

if kg_morango <= 5:
    total_morango = kg_morango * 2.50
else:
    total_morango = kg_morango * 2.20

if kg_maca <= 5:
    total_maca = kg_maca * 1.80
else:
    total_maca = kg_maca * 1.50

valor_bruto = total_morango + total_maca
peso_total = kg_morango + kg_maca

if peso_total > 8 or valor_bruto > 25:
    valor_final = valor_bruto * 0.90
else:
    valor_final = valor_bruto

print(f"Valor final a pagar: R$ {valor_final:.2f}")