x = lambda y : y + 10
print(x(5))

x = lambda x, y : x * y
print(x(10, 3))

x = lambda x, y, z : x + y + z
print(x(10, 10, 30))

def nome_funcao(n):
    return lambda a : a * n
multiplicador = nome_funcao(5)
print(multiplicador(10))

lista = [1, 5, 4, 6, 8, 11, 3, 12]
nova_lista = list(filter(lambda x: (x%2 == 0), lista))
print(nova_lista)
