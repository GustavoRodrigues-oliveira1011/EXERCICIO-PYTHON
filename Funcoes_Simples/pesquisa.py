print("\n--- Teste da segunda função de pesquisa ('pesquisa') ---")

def pesquisa(lista, nome):
    """
    Pesquisa um valor em uma lista e retorna seu índice ou -1 se não encontrado.
    """
    for x, e in enumerate(lista):
        if e == nome:
            return x
    return -1

nome = input("Digite seu nome para verificar na lista: ")

L = ["Alice", "Bob", "Charlie", "David", "Gustavo"]

print(f"Pesquisando seu nome na lista")

if pesquisa(L, nome) == -1:
    print(f"Acesso negado! Seu nome não está na lista.")
else:
    print(f"Acesso autorizado! Seu nome está na lista: {pesquisa(L, nome)}")