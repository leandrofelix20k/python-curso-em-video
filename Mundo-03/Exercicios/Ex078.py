'''
Faça um programa que leia 5 valor numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado as 
suas respectivas posições na lista
'''

numeros = []
print('Digite cinco valores: ')
for i in range(0, 5):
    numeros.append(int(input(f'{i+1}°Posição: ')))

maior = max(numeros)
menor = min(numeros)

print(f'Valores digitados {numeros}')
print(f'Maior número é o {maior}, na posição', end= ' ')
for j in range(0, 5):
    if maior == numeros[j]:
        print(f'{j+1}', end= ' ')
print(f'\nMenor número é o {menor}, na posição', end= ' ')
for k in range(0, 5):
    if menor == numeros[k]:
        print(f'{k+1}', end=' ')
print('\n')
