import numpy as np

# os indices no python vao de 0 a n-1
# onde n é o tamanho da dimensao
x = np.linspace(start=10, stop=100, num=10)
print("\nx:", x)
print("shape:", x.shape)

# extracao de elementos
print("\nx:", x)
print("primeiro elemento:", x[0])
print("segundo elemento:", x[1])
print("ultimo elemento:", x[9])
print("ultimo elemento:", x[-1])

# slicing: extracao de subarrays
print("\nx:", x)
print("dois primeiros elementos:", x[0:2])
print("dois primeiros elementos:", x[:2])
print("dois ultimos elementos", x[-2:])

# slicing em arrays 2d (matrizes)
x = x.reshape(2, 5) # reshape de x para 2 linhas e 5 colunas
print("\nx:\n", x)

# extracao de elementos
print("primeira linha, segunda coluna:", x[0, 1])
print("segunda linha, penultima coluna:", x[1, -2])
print("ultima linha, ultima coluna:", x[1, 4])
print("ultima linha, ultima coluna:", x[-1, -1])

# slicing: extracao de subarrays
print("\nx:\n", x)
print("primeira linha inteira: ", x[0, :])
print("primeira linha, segunda a quarta coluna: ", x[0, 1:4])
print("ultima coluna inteira:\n", x[:, [-1]])

# atencao com compartilhamento de memoria em subarrays
x = np.array([1, 2, 3])
print("\nx antes:", x)
y = x[:2]
y[0] = 100 # alteracao do valor em y altera o valor de x
print("x depois:", x)

# atencao com compartilhamento de memoria em subarrays (evitar gerando copy)
x = np.array([1, 2, 3])
print("\nx antes:", x)
y = x[:2].copy()
y[0] = -100 # alteracao do valor em y altera o valor de x
print("x depois:", x)



