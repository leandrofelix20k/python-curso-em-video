#Desafio 82

'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
numPares = []
numImpares = []


print('*Caso queira parar, digite -1 a qualquer momento!\n')
cont = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    if numeros[cont] == -1:
        numeros.remove(-1)
        break
    cont += 1

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        numPares.append(numeros[i])
    else:
        numImpares.append(numeros[i])
    i += 1

print('-=' * 10)
print(f'Números digitados: {numeros}')
print(f'Números pares: {numPares}')
print(f'Números ímpares: {numImpares}')
