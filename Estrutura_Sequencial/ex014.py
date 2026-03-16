peso = float(input('Digite o Peso da balança: '))
excesso = float (peso) - 50
multa = float (excesso) * 4

print('------------------------------- ')
print(f'Peso da balança: {peso:.2f} KG ')
print('------------------------------- ')

if peso >= 50:
    print(f'Balança excedida em {excesso:.2f} KG')
    print(f'Valor da Multa de R${multa:.2f} reais')
    print('------------------------------- ')
else:
    print(f'Balança dentro do limite!')
    print(f'Valor da balaça: {peso:.2f} KG')
    print('------------------------------- ')

  