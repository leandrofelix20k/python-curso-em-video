'''
Crie um programa que tenha uma tupla preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e vinte)
e mostrá-lo por extenso
'''

numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
        'treze',  'quatorze', 'quinze', 'dezesseis', 'dezesete', 
        'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Tente Novamente..', end= '')
        else:
            break
    print('O número {} por extenso é {}'.format(num, numExtenso[num]))
    perg = str((input('*Deseja continuar[S/N]? '))).upper().strip()[0]
    if perg == 'N':
        print('VOLTE SEMPRE!')
        break
