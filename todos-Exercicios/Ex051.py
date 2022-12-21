#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-' * 5, 'PROGRESSÃO ARITIMÉTICA(P.A.)', '-' * 5)

primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite agora a razão da PA: '))
ultiTermo = primTermo + (razao * 10)
termoAtual = primTermo

print('Os 10 primeiros termos dessa progressão são:')
for i in range(0, 10):
    print('{}'.format(termoAtual))
    termoAtual += razao
    