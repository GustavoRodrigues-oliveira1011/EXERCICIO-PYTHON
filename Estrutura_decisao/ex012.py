valor_hora = float(input("Valor da sua hora: R$ "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    percentual_ir = 0
elif salario_bruto <= 1500:
    percentual_ir = 5
elif salario_bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

ir = salario_bruto * (percentual_ir / 100)
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("-" * 30)
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%): R$ {ir:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"(-) Sindicato (3%): R$ {sindicato:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
