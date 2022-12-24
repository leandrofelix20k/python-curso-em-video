#Desafio 78

'''
Faça um programa que leia 5 valor numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado as 
suas respectivas posições na lista
'''

numeros = []
print('Digite cinco valores: ')
for i in range(0, 5):
    numeros.append(int(input()))

maior = max(numeros)
posMaior = numeros.index(maior)
menor = min(numeros)
posMenor = numeros.index(menor)

print(f'Maior número {maior} está na {posMaior+1}°posição')
print(f'Menor número {menor} está na {posMenor+1}°posição')
