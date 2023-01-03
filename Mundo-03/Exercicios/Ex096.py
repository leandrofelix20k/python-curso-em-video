'''
Faça um programa que tenha uma função chamada área(). que receba as
dimensões de um terreno retangular (largura e comprimenro) e mostre
a área do terreno.
'''

def area(l, c):
    a = l * c
    print(f'A área do retângulo é igual a {a:.1f}m².')
    

largura = float(input('Digite a largura do retângulo: '))
comprimento = float(input('Digite o comprimento do retângulo: '))

area(largura, comprimento)
