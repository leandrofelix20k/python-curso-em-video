#Desafio 50

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas saqueles que forem pares. Se o valor digitado for ímpar, desconsider-o.

print('Digite pelo menos, seis números pares.')
num = int(input('Digite um número: '))
pares = 6
soma = 0
j = 0

for i in range(j, pares):
    if(num % 2 == 0):
        soma += num
        j += 1
    else:
        pares += 1
    num = int(input('Digite mais um número: '))

print('A soma dos números pares digitados foi: {}'.format(soma))
        