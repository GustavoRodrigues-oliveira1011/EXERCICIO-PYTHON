litros = float(input("Quantidade de litros vendidos: "))
tipo = input("Tipo de combustível (A-álcool, G-gasolina): ").upper()

if tipo == "A":
    preco_base = 1.90
    if litros <= 20:
        percentual_desconto = 0.03 # 3%
    else:
        percentual_desconto = 0.05 # 5%
    
    
    valor_final = litros * (preco_base * (1 - percentual_desconto))
    print(f"Total a pagar (Álcool): R$ {valor_final:.2f}")

elif tipo == "G":
    preco_base = 2.50
    if litros <= 20:
        percentual_desconto = 0.04 # 4%
    else:
        percentual_desconto = 0.06 # 6%
    
    valor_final = litros * (preco_base * (1 - percentual_desconto))
    print(f"Total a pagar (Gasolina): R$ {valor_final:.2f}")

else:
    print("Tipo de combustível inválido!")