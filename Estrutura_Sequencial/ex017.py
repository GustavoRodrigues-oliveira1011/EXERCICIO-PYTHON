area = float(input("Digite a área: "))

litros = (area / 6) * 1.1

latas_so = int(litros / 18 + 0.99)
preco_so_latas = latas_so * 80

galoes_so = int(litros / 3.6 + 0.99)
preco_so_galoes = galoes_so * 25

latas_mix = int(litros // 18)
resto = litros % 18

galoes_mix = int(resto / 3.6 + 0.99)

if (galoes_mix * 25) > 80:
    latas_mix += 1
    galoes_mix = 0

print(f"Mistura: {latas_mix} latas e {galoes_mix} galões. Total: R$ {(latas_mix * 80) + (galoes_mix * 25):.2f}")