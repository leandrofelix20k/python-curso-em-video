#Desafio 28

#Faça um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

import random


print('\t---Jogo da advinhação---')
print('Computador Pensando em número entre 0 e 5...')
numAleatorio = random.randint(0, 5)
num = int(input('Tente adivinhar o número que o computador pensou: '))

if(num == numAleatorio):
    print('Parabéns, Vocẽ Acertou!')
else:
    print('Quase! O número pensado pelo computador foi {}'.format(numAleatorio))
