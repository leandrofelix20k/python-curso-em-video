#Desafio 100

'''
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteio() e somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados
'''

from random import randint
from time import sleep

def sorteio(num):
    print('Sorteando 5 valores: ')
    sleep(1)
    for i in range(0, 5):
        num.append(randint(0, 10))
        print(num[i], end= ' ')
    print('PRONTO!')


def somaPar(num):
    soma = 0
    for i in range(0, 5):
        if num[i] % 2 == 0:
            soma += num[i]
    print(f'Somando os valores pares de {num}, temos {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)