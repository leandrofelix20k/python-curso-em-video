'''
Melhore o Desafio 61, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser
que quer mostar 0 termos
'''

print('-' * 5, 'PROGRESSÃO ARITIMÉTICA(P.A.)', '-' * 5)
primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite agora a razão da PA: '))
termoAtual = primTermo

termos = int(input('Quantos termos da PA você quer? '))
cont = 0
while termos != 0:
    while cont < termos:
        print('{}'.format(termoAtual))
        termoAtual += razao
        cont += 1
    termos = int(input('Deseja mostrar mais quantos termos dessa PA? '))
    cont = 0
    