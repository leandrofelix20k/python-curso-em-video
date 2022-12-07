#Desafio 68

'''
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador perder, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo
'''

from random import randint

cond = False
cont = 0

print('=-' * 14)
print('PAR OU ÍMPAR')
print('=-' * 14)
while cond == False:
    numUsuario = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar[P/I]? ')).upper()
    while escolha != 'P' and escolha != 'I':
        print('Opção Invalida!')
        escolha = str(input('Digite "P" para PAR e "I" para ÍMPAR: ')).upper()
    numComputador = randint(1, 10)
    soma = numUsuario + numComputador
    resto = (numUsuario + numComputador) % 2

    if resto == 0:
        print('--' * 14)
        print(f'Você escolheu o número {numUsuario} e o computador {numComputador}. O total de {soma} DEU PAR!')
        print('--' * 14)
        if escolha == 'P':
            print('Você VENCEU!')
            print('Vamos mais uma partida...')
            print('=-' * 14)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 14)
            cond = True
    else:
        print('--' * 14)
        print(f'Você escolheu o número {numUsuario} e o computador {numComputador}. O total de {soma} DEU ÍMPAR!')
        print('--' * 14)
        if escolha == 'I':
            print('Você VENCEU!')
            print('Mais uma partida...')
            print('=-' * 14)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 14)
            cond = True
        
    if cond == True:
        print(f'GAME OVER! Você ganhou {cont} vezes consecutivas.')
