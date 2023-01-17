#Desafio109

'''
Adapte o desafio 108, criando uma função adicional chamada moeda que
consiga mostrar os valores como um valor monetário formatado.
'''

import moedas

p = float(input('Digite o preco: R$'))
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moedas.diminuir(p, 13, True)}')
print(f'O dobro de {moedas.moedas(p)} é {moedas.dobro(p)}')
print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p)}')
