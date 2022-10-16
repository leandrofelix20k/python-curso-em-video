#Desafio 46

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com um de 1 segundo entre eles

from time import sleep

print('\n')
print('-=' * 18)
print('-=Iniciando a contagem regressiva!-=')
print('-=' * 18, '\n')

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('KABUUM!')