#Desafio 107


'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas
funções.
'''

import moedas

p = float(input('Digite o preco: R$'))
print(f'Aumentando 10%, temos R${moedas.aumentar(p, 10):.2f}')
print(f'Diminuindo 13%, temos R${moedas.diminuir(p, 13):.2f}')
print(f'O dobro de {p} é R${moedas.dobro(p):.2f}')
print(f'A metade de {p} é R${moedas.metade(p):.2f}')
