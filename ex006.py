import numpy as np 

array_A = np.array([10, 20, 30, 40])
array_B = np.array([2, 2, 5, 10])

# O grande poder do NumPy: ele faz as contas com as listas inteiras
# elemento por elemento, sem precisar usar um loop "for"!
print("Soma:", array_A + array_B)
print("Subtração:", array_A - array_B)
print("Multiplicação:", array_A * array_B)
print("Divisão:", array_A / array_B)