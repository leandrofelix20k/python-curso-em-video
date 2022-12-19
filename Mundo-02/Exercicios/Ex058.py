'''
Melhore o jogo Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
'''

import random
from time import sleep

acertou = 0
cont = 1
print('\t---Jogo da advinhação---')
print('Computador Pensando em número entre 0 e 10...')
sleep(3)
print('Pronto!')
numAleatorio = random.randint(0, 10)
num = int(input('Tente adivinhar o número que o computador pensou: '))
while acertou == 0:
    if(num == numAleatorio):
        acertou = 1
    else:
        print('\n')
        if num < numAleatorio:
            num = int(input('Mais! Digite um novo palpite: '))
        else:
            num = int(input('Menos! Digite um novo palpite: '))
    cont += 1

print('\n')
print('Parabéns, Vocẽ Acertou!')
print('Número de tentativas = ', cont)