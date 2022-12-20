#Desafio 72

'''
Crie um programa que tenha uma tupla preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e vinte)
e mostrá-lo por extenso
'''

numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis' , 
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',  'quatorze', 
'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente Novamente... Digite um número entre 0 e 20: '))

print('O número {} por extenso é {}'.format(num, numExtenso[num]))
