#Desafio 71

'''
Crie um programa que simule um caixa eletrônico. No início,
pergunte ao usuário qual será o valor sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e
R$1
'''
print('=-' * 10)
print(' '* 2, 'BANCO TABAJARAS')
print('=-' * 10)

valor = str(input('Digite quanto você deseja sacar: '))
valorInt = int(valor)
tamValor = len(valor)

unidade = valor[tamValor-1]
dezena = valor[tamValor-2:]
centena = valor[tamValor-3:]

if valorInt > 50:
    if valorInt < 100 and valorInt >=50:
        cedCinquenta =  1
    else:
        if int(dezena) >= 50:
            cedCinquenta = (int(valor[0:tamValor-2]) * 2) + 1
        else:
            cedCinquenta = int(valor[0:tamValor-2]) * 2
    print(f'Total de {cedCinquenta} cédula(s) de R$50')
if int(dezena) > 0:
    if int(dezena) < 50:
        if (int(valor[tamValor-2]) % 2) == 0:
            cedVinte = int(valor[tamValor-2]) / 2
            print('Total de {:.0f} cédula(s) de R$20'.format(cedVinte))
        else:
            if int(valor[tamValor-2]) == 1:
                print('Total de 1 cédula de R$10')
            else:
                cedVinte = int(valor[tamValor-2]) - 2
                print('Total de {:.0f} cédula(s) de R$20'.format(cedVinte))
                print('Total de 1 cédula de R$10')
    elif int(dezena) >= 60: 
        dezena = int(dezena[0]) - 5
        if dezena % 2 == 0:
            cedVinte = dezena / 2
            print('Total de {:.0f} cédula(s) de R$20'.format(cedVinte))
        else:
            if dezena == 1:
                print('Total de 1 cédula de R$10')
            else:
                cedVinte = dezena - 2
                print('Total de {:.0f} cédula(s) de R$20'.format(cedVinte))
                print('Total de 1 cédula de R$10')
if int(unidade) > 0:
    print(f'Total de {unidade} cédula(s) de R$1')
