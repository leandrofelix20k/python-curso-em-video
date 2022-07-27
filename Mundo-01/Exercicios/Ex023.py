#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
 
num = str(input('Digite um número entre 0 e 9999: '))
numInt = int(num)
lista = num.split()

if(numInt > 999):
    print('Unidade: {}'.format(lista[0][3]))
if(numInt > 99):
    print('Dezena: {}'.format(lista[0][2]))
if(numInt > 9):
    print('Centena: {}'.format(lista[0][1]))
if(numInt > 0):
    print('Milhar: {}'.format(lista[0][0]))
    