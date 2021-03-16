import random
min = 1 # Valor mínimo que um dado pode mostrar
max = 6 # Valor máximo que um dado pode mostrar

jogar_novamente = 'sim'

while jogar_novamente == 'sim':
    print ('Jogando os dados...')
    print ('Os valores são....')
    print (random.randint(min, max))
    print (random.randint(min, max))

    jogar_novamente = input('Jogar os dados mais uma vez? [SIM / NÃO]\n').lower()
