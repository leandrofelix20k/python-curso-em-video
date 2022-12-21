'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonnaci
'''

print('-' * 5, 'Sequência de Fibonacci', '-' * 5)
n = int(input('Digite quantos elementos da Sequência de Fibonacci você deseja: '))
cont = 0
elementoAtual = 0
proxElemento = 1
elementoAnterior = elementoAtual
print('{} '.format(elementoAtual), end='')

while cont < n-1:
    elementoAtual = proxElemento
    print('-> {} '.format(elementoAtual), end='')
    proxElemento = elementoAtual + elementoAnterior
    elementoAnterior = elementoAtual
    cont += 1
print('\n')
