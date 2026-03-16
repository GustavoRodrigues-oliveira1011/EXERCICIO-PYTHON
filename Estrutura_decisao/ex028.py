print("1 - File Duplo | 2 - Alcatra | 3 - Picanha")
opcao = input("Escolha o tipo de carne (1, 2 ou 3): ")
qtd = float(input("Quantidade (Kg): "))
cartao = input("Pagamento no cartão Tabajara? (S/N): ").upper()

if opcao == "1":
    nome_carne = "File Duplo"
    preco_kg = 4.90 if qtd <= 5 else 5.80
elif opcao == "2":
    nome_carne = "Alcatra"
    preco_kg = 5.90 if qtd <= 5 else 6.80
else:
    nome_carne = "Picanha"
    preco_kg = 6.90 if qtd <= 5 else 7.80

preco_total = qtd * preco_kg
desconto = preco_total * 0.05 if cartao == "S" else 0
valor_pagar = preco_total - desconto

print("\n--- CUPOM FISCAL ---")
print(f"Item: {nome_carne}")
print(f"Quantidade: {qtd} Kg")
print(f"Preço Total: R$ {preco_total:.2f}")
print(f"Tipo de Pagamento: {'Cartão Tabajara' if cartao == 'S' else 'Dinheiro/Outros'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_pagar:.2f}")