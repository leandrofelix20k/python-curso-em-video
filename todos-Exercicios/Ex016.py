#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 

from math import floor

num = float(input('Digite um número Real qualquer: '))

print('A parte inteira do número {} é igua a {}'.format(num, floor(num)))
