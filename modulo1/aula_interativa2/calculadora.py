def adicao(a, b):
    sum = a + b
    return sum

def subtracao(a, b):
    diff = a - b
    return diff

def multiplicacao(a, b):
    multi = a*b
    return multi

def divisao(a, b):
    divi = a/b
    return divi

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print('\n\nA soma entre os números é:', adicao(a,b))
print('A diferença entre os número é:', subtracao(a,b))
print('A multiplicação entre os números é:', multiplicacao(a,b))
print('A divisão entre os números é:', divisao(a,b))
