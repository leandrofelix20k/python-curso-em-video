#Desafio 74

'''
Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla.

Depois disso, mostre a listagem de números gerados e também indique 
o menor e o maior valor que estão na tupla.
'''

from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('O valores sorteados foram: {}'.format(valores))
for i in range(0, 5):
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
