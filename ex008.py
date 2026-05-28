import numpy as np  


array_12 = np.arange(1, 13)
print("Array Original (1D):", array_12)


matriz_3x4 = array_12.reshape(3, 4)
print("\nMatriz 3x4:\n", matriz_3x4)

matriz_2x6 = array_12.reshape(2, 6)
print("\nMatriz 2x6:\n", matriz_2x6)