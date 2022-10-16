#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
cont = 0

for i in range(num, 0, -1):
    if(num % i == 0):
        cont += 1

if(cont == 2):
    print('O número que você digitou é primo!')
else:
    print('O número que você digitou não é primo!')
    