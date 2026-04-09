def eh_par(numero):
    return numero % 2 == 0

def eh_impar(numero):
    return numero % 2 !=0

def verificar_numero(numero):
    
    if eh_par(numero):
        print(f"O número {numero} é PAR")
    else:
        print(f"O número {numero} é ÍMPAR")

def pegar_entrada():
    entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")
    return entrada 

def interagir_com_usuario():
    print("--- Verificador de Números Pares e Ímpares ---")
    while True:
        entrada = pegar_entrada()
        
        if entrada.lower() == 'sair':
            print("Até logo!")
            break
        
        try:
            numero = int(entrada)
            verificar_numero(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")

if __name__ == "__main__":
    interagir_com_usuario()