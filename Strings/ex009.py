cpf_bruto = input("Digite o CPF (xxx.xxx.xxx-xx): ")
cpf = cpf_bruto.replace(".", "").replace("-", "")

# --- CÁLCULO DO 1º DÍGITO ---
soma = 0
for i in range(9):
    # i começa em 0. Para o peso começar em 10, fazemos (10 - i)
    soma += int(cpf[i]) * (10 - i)

digito1 = (soma * 10) % 11
if digito1 >= 10: digito1 = 0

# --- CÁLCULO DO 2º DÍGITO ---
soma = 0
for i in range(10):
    # i começa em 0. Para o peso começar em 11, fazemos (11 - i)
    soma += int(cpf[i]) * (11 - i)

digito2 = (soma * 10) % 11
if digito2 >= 10: digito2 = 0

if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
    print("CPF Válido!")
else:
    print("CPF Inválido!")