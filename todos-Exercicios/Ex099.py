'''
Faça um programa que tenha uma função chamada maior, que receba
vários parâmetros com valores inteiros

Seu programa tem que analisar todos os valores e dizer qual é o
maior deles.
'''

from random import randint
from time import sleep

def mostraLinha():
    print('=-=' * 15)

def maior(values):
    mostraLinha()
    print('Analisando valores passados...')
    for i in range(0, len(valores)):
        print(f'{valores[i]}', end= ' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')

    for i in range(0, len(valores)):
        if i == 0:
            m = valores[i]
        else:
            if valores[i] > m:
                m = valores[i]
    if m > 0:
        print(f'O maior valor informado foi {m}')
    else:
        print('Nenhum valor foi passado!')


for i in range(0, 5):
    quantidade = randint(1, 10)
    valores = []

    for j in range(0, quantidade):
        valores.append(randint(0, 10))
    maior(valores)
 