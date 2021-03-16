# Importa a função randint que retorna um valor aleatório
from random import randint

# Cria uma lista com as Opções
t = ['pedra', 'papel', 'tesoura'] #Editei o codigo original deixando minusculo para poder ser escrito de qualquer maneira e reconhecer.

# Coloca o computador para jogar dentro das opções
computador = t[randint(0, 2)]

# Coloca o jogador como False
jogador = False

while jogador == False:
    jogador = input('Pedra, Papel, Tesoura? ').lower() #Desde que esteja escrito corretamente vai aceitar mesmo em minusculo, maiusculo ou misturado.
    if jogador == computador:
        print('Empate!')
    elif jogador == 'pedra':
        if computador == 'papel':
            print('Você Perdeu', computador, 'embrulha', jogador)
        else:
            print('Você venceu!', jogador, 'esmaga', computador)
    elif jogador == 'papel':
        if computador == 'tesoura':
            print('Você Perdeu', computador, 'corta', jogador)
        else:
            print('Você venceu!', jogador, 'embrulha', computador)
    elif jogador == 'tesoura':
        if computador == 'pedra':
            print('Você Perdeu', computador, 'esmaga', jogador)
        else:
            print('Você venceu!', jogador, 'corta', computador)
    else:
        print('Essa não é uma jogada válida. Verifique a ortografia!')

    # Para continuar o jogo
    jogador = False
    computador = t[randint(0, 2)]
