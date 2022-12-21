#Crie um programa que faça o computador jogar Jokenpô com você

import random
from time import sleep

print('-' * 8, end= '')
print('JOKÊNPÔ', end= '')
print('-' * 8)
print('Vamos Jogar Jokênpô! Escolha uma das opções abaixo:')
escolhaJogador = int(input('1-Pedra\n2-Papel\n3-Tesoura\nOpção: '))

jogarNovamente = 1
while(jogarNovamente == 1):
    print('JO')
    sleep(1)
    print('KÊN')
    sleep(1)
    print('PÔ')
    random.seed()
    escolhaComp = random.randint(1, 3)
    print('\n', '-' * 45)
    if(escolhaComp == 1):
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Pedra!\n EMPATE!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Pedra!\n O Jogador VENCEU!')
        else:
            print('A escolha do computador foi: Pedra!\n O Computador VENCEU!')
    if(escolhaComp == 2):
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Papel!\n O Computador VENCEU!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Papel!\n EMPATE!')
        elif(escolhaJogador == 3):
            print('A escolha do computador foi: Papel!\n O Jogador VENCEU!')
    if(escolhaComp == 3):
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Tesoura!\n O Jogador VENCEU!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Tesoura!\n O Computador VENCEU!')
        elif(escolhaJogador == 3):
            print('A escolha do computador foi: Tesoura!\n EMPATE!')
    print('-' * 45)

    jogarNovamente = int(input('Deseja jogar novamente? \n1- Sim\n2- Não\nOpção: '))
    if(jogarNovamente == 1):
        print('-' * 8, end= '')
        print('Escolha uma das opções abaixo:',end= '')
        print('-' * 8)
        escolhaJogador = str(input('1-Pedra\n2-Papel\n3-Tesoura\nOpção: '))
    else:
        print('Obrigado! Volte Sempre!')
        jogarNovamente = 0
        