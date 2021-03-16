import random

# Uma função que embaralha todos os caracteres de uma string
def embaralha(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# Gerar letras aleatórias
letra_1=chr(random.randint(65,90)) # Gere uma letra maiúscula aleatória (com base no código ASCII)
letra_2=chr(random.randint(65,90)) # Gere uma letra maiúscula aleatória (com base no código ASCII)
# Continue aqui a geração de letras. Copie e cole a linha acima mudando o nome da variável


# Gere senha usando todos os caracteres, em ordem aleatória
password = letra_1 + letra_2    # Concatene outras letras
password = embaralha(password)

# Saída
print(password)
