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
    escolha = str(input('Par ou Ímpar[P/I]? ')).upper().strip()[0]
    while escolha not in 'PI':
        print('Opção Invalida!')
        escolha = str(input('Digite "P" para PAR e "I" para ÍMPAR: ')).upper().strip()[0]
    numComputador = randint(1, 10)
    soma = numUsuario + numComputador
    resto = (numUsuario + numComputador) % 2
    print('--' * 14)
    print(f'Você escolheu o número {numUsuario} e o computador {numComputador}! O total de {soma}')
    print('DEU ÍMPAR!' if resto != 0 else 'DEU PAR!')
    print('--' * 14)

    if resto == 0:
        if escolha == 'P':
            print('Você VENCEU!\nMais uma partida...')
            print('=-' * 14)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 14)
            cond = True
    else:
        if escolha == 'I':
            print('Você VENCEU!\nMais uma partida...')
            print('=-' * 14)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 14)
            cond = True
        
    if cond == True:
        print(f'GAME OVER! Você ganhou {cont} vez(es) consecutiva(s).')
