salario_bruto = float(input('Digite o seu salario bruto: '))
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salario Bruto: R${salario_bruto:.2f} Reais')
print(f'O Seu salario Liquido é de: R${salario_liquido:.2f} Reais')
print('Descontos:')
print(f'IR: R${ir:.2f} Reais')
print(f'INSS: R${inss:.2f} Reais')