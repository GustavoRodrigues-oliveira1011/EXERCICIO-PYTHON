nome1 = input("Digite seu nome: ")
nome2 = input("Digite seu nome: ")

print(f"'{nome1}': {len(nome1)} caracteres")
print(f"'{nome2}': {len(nome2)} caracteres")

if len(nome1) == len(nome2):
    print("Possuem o mesmo tamanho.")
else:
    print("Tamanhos da strings são diferentes.")

if nome1 == nome2:
    print("Conteúdo igual.")
else:
    print("Conteúdo diferente.")

