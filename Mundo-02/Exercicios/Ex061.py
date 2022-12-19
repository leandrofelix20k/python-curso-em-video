'''
Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura
while
'''

print('-' * 5, 'PROGRESSÃO ARITIMÉTICA(P.A.)', '-' * 5)
primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite agora a razão da PA: '))
termoAtual = primTermo
cont = 0

print('Os 10 primeiros termos dessa progressão são:')
while cont < 10:
    print('{}'.format(termoAtual))
    termoAtual += razao
    cont += 1
    