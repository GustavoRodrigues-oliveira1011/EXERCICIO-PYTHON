n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar (+, -, *, /): ")

if operacao == "+": resultado = n1 + n2
elif operacao == "-": resultado = n1 - n2
elif operacao == "*": resultado = n1 * n2
elif operacao == "/": resultado = n1 / n2
else: 
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    par_impar = "par" if resultado % 2 == 0 else "ímpar"
    
    pos_neg = "positivo" if resultado >= 0 else "negativo"
    
    int_dec = "inteiro" if resultado == round(resultado) else "decimal"
    
    print(f"\nResultado: {resultado}")
    print(f"O número é: {par_impar}, {pos_neg} e {int_dec}.")