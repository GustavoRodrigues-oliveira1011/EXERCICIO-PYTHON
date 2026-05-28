import numpy as np

dados = np.array([5, 12, 8, 20, 3, 15, 7, 30])


mascara_maior_que_10 = dados > 10

filtrado = dados[mascara_maior_que_10]


print("Dados originais:", dados)
print("Apenas os maiores que 10:", filtrado)