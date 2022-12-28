'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpite.
O prgrama vai perguntar quantos jogo serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
'''

from random import randint 
from time import sleep

print('-' * 34)
print('{:-^34}'.format('GERADOR DE NÚMEROS'))
print('{:-^34}'.format('PARA A MEGA SENA'))
print('-' * 34)

quantidade = int(input('Quantos jogo você quer que eu sorteie? '))
jogo = []
todosjogo = []

for l in range(0, quantidade):
    c = 0
    while c < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            c += 1
    jogo.sort()
    todosjogo.append(jogo[:])
    jogo.clear()

for i in range(0, len(todosjogo)):
    sleep(1.5)
    print(f'Jogo {i+1}: {todosjogo[i]}')

print('\n{:-^32}'.format('Boa Sorte!'))
