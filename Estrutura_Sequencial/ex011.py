n1= int (input('Digite um numero inteiro:'))
n2= int (input('Digite um numero real:'))
n3= float(input('Digite um numero real:').replace (',','.'))
a =  (2 * n1) * (n2 /2)
b = ( 3 * n1) + n3
c = n3 ** 3

print(f'Resultado A: {a}')
print(f'Resultado B: {b}')
print(f'Resultado C: {c:.2f}')  