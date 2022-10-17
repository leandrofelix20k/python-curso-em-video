#Desafio 55 

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('Digite o peso de cinco pessoas em Kg: ')

menorPeso = 10000
maiorPeso = 0
for i in range(0, 5):
    peso = float(input('Pessoas N°{}: '.format(i+1)))
    if(peso < menorPeso):
        menorPeso = peso
    if(peso > maiorPeso):
        maiorPeso = peso

print('\nO maior peso dentre essa cincos pessoas é: {:.1f}Kg'. format(maiorPeso))
print('O menor peso é: {:.1f}kg'.format(menorPeso))

'''
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Pessoas N°{}: '.format(i+1)))
    if i == 0:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
'''
