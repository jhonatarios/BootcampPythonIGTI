import numpy as np

#criacao de um array 1D: [1, 2, 3]
l = [1, 2, 3]
x = np.array(l)
print("x:\n", x)
print("shape:", x.shape)

#criacao de um array 2D: listas aninhadas
l = [[1, 2], [3, 4]]
x = np.array(l)
print("x:\n", x)
print("shape:", x.shape)

#array contendo apenas 0's
dim = (2, 2) # (linhas, colunas)
x = np.zeros(dim)
print("x:\n", x)
print("shape:", x.shape)

#array contendo apenas 1's
size = (2, 2) # (linhas, colunas)
x = np.ones(size)
print("x:\n", x)
print("shape:", x.shape)

#criacao de valores dentro de um intervalo
#valores uniformes entre 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print("x:\n", x)
print("shape:", x.shape)

#criacao de matriz identidade
n = 4
x = np.eye(n)
print("x:\n", x)
print("shape:", x.shape)

#criacao de valores aleatorios
#np.random.seed(10)
x = np.random.random(size=(2, 3))
print("x:\n", x)
print("shape:", x.shape)
