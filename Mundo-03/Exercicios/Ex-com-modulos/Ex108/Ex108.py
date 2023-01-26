'''
Adapte o desafio 108, criando uma função adicional chamada moeda que
consiga mostrar os valores como um valor monetário formatado.
'''

import moedas

p = float(input('Digite o preco: R$'))
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
