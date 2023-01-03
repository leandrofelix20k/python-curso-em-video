'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem pesonalizada
'''

from time import sleep

def mostraLinha():
    print('=-=' * 12)

    
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f}, de {p} em {p}:')
    if i < f:
        for j in range(i, f, p):
            print(f'{j}', end=  ' ', flush= True)
            sleep(0.1)
    else:
        for j in range(i, f, -p):
            print(f'{j}', end= ' ', flush= True)
            sleep(0.1)
    print('\nFIM!')
        

mostraLinha()
contador(1, 10, 1)
mostraLinha()

contador(10, 0, -2)
mostraLinha()

print('Sua vez agora!')
incio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
mostraLinha()

contador(incio, fim, passo)
