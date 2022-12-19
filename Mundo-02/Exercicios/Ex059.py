'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''---Selecione um Opção:---
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    opcao = int(input('Operação: '))
    
    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 == num2:
            print('Os números são iguais!')
        if num1 > num2:
            print('O número {} é maior que {}'.format(num1, num2))
        else:
            print('O número {} é maior que {}'.format(num2, num1))
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('\n\n')
        print('---Até Uma Próxima!---')
    else:
        print('\n\n')
        print('-Operação inválida! Digite Novamente:-')
    print('\n\n')
    