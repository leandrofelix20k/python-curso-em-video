#Desafio 09

#Faça um programa que leia um número qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número: '))
simbolo = '=' * 10

print('{} Tabuada do número {} {}'.format(simbolo, num, simbolo))

print('{}x1 = {}'.format(num, num * 1))
print('{}x2 = {}'.format(num, num * 2))
print('{}x3 = {}'.format(num, num * 3))
print('{}x4 = {}'.format(num, num * 4))
print('{}x5 = {}'.format(num, num * 5))
print('{}x6 = {}'.format(num, num * 6))
print('{}x7 = {}'.format(num, num * 7))
print('{}x8 = {}'.format(num, num * 8))
print('{}x9 = {}'.format(num, num * 9))
print('{}x10 = {}'.format(num, num * 10))

print(simbolo * 4)