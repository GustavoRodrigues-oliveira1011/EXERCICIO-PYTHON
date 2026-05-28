import numpy as np

aleatorios = np.random.randint(1, 100, 20)
print("Array gerado:", aleatorios)

print("Valor Máximo:", np.max(aleatorios))
print("Valor Mínimo:", np.min(aleatorios))
print("Média:", np.mean(aleatorios))
print("Soma Total:", np.sum(aleatorios))