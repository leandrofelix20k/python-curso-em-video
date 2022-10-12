#Desafio 45

#Crie um programa que faça o computador jogar Jokenpô com você

import random

print('-' * 8, end= '')
print('JOKÊNPÔ', end= '')
print('-' * 8)
print('Vamos Jogar Jokênpô! Escolha uma das opções abaixo:')
escolhaJogador = str(input('1-Pedra\n2-Papel\n3-Tesoura\nOpção:'))

jogarNovamente = 1
while(jogarNovamente == 1):
    random.seed()
    escolhaComp = random.randint(1, 3)
    print('\n', '-' * 45)
    if(escolhaComp == 1):
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Pedra! EMPATE!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Pedra! VITÓRIA!')
        else:
            print('A escolha do computador foi: Pedra! DERROTA!')
    elif(escolhaComp == 2):
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Papel! VITÓRIA!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Papel! EMPATE!')
        else:
            print('A escolha do computador foi: Papel! DERROTÁ!')
    else:
        if(escolhaJogador == 1):
            print('A escolha do computador foi: Tesoura! DERROTA!')
        elif(escolhaJogador == 2):
            print('A escolha do computador foi: Tesoura! VITÓRIA!')
        else:
            print('A escolha do computador foi: Tesoura! EMPATE!')
    print('-' * 45)

    jogarNovamente = int(input('Deseja jogar novamente? \n1- Sim\n2- Não\nOpção: '))
    if(jogarNovamente == 1):
        print('-' * 8, end= '')
        print('Escolha uma das opções abaixo:',end= '')
        print('-' * 8)
        escolha = str(input('1-Pedra\n2-Papel\n3-Tesoura\nOpção: '))
    else:
        print('Obrigado! Volte Sempre!')
        