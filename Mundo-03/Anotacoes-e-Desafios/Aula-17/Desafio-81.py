#Desafio 81

'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado de forma decrescente e está ou na lista.
'''

numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))

    perg = str(input('Desseja continuar[S/N]? ')).upper().strip()[0]
    if perg == 'N':
        break
    
print(f'\n>Foram digitados {len(numeros)} números')
numeros.sort(reverse= True)
print(f'>Lista na ordem descrescente{numeros}')
if 5 in numeros:
    print(f'>O número 5 está na lista! Ele foi digitado {numeros.count(5)} vez(es)')
else:
    print('>O número 5 não está na lista!')
