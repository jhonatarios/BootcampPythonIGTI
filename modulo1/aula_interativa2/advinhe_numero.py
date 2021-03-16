import random

n = random.randint(1, 99)

advinhe = int(input("Tente advinhar um numero entre 1 e 99: "))

while n != "advinhe":
    if advinhe < n:
        print("O numero é maior que este")
        advinhe = int(input("Tente outra vez: "))
    elif advinhe > n:
        print("O numero é menor que este")
        advinhe = int(input("Tente outra vez: "))
    else:
        print("Você acertou!")
        break
