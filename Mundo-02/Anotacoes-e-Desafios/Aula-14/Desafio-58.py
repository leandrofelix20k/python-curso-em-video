#Desafio 58

#Melhore o jogo Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random
from time import sleep

acertou = 0
cont = 1
while acertou == 0:
    print('\t---Jogo da advinhação---')
    print('Computador Pensando em número entre 0 e 10...')
    sleep(3)
    print('Pronto!')
    numAleatorio = random.randint(0, 3)
    num = int(input('Tente adivinhar o número que o computador pensou: '))

    if(num == numAleatorio):
        print('Parabéns, Vocẽ Acertou!')
        print('Número de tentativas = ', cont)
        acertou = 1
    else:
        print('Errou! O número pensado pelo computador foi {}'.format(numAleatorio))
    cont += 1
    sleep(2)
    print('\n\n\n')
