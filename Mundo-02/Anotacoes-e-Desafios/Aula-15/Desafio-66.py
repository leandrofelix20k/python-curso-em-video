#Desafio 66

'''
Crie um programa que leia vários números inteiros pelos teclado. 
O programa só vai parar quando o usuário  digitar  o valor 999, 
que é a condição de parada. No final, mostre quantos números 
forma digitados e qual foi a soma entre eles desconsiderando o flag.
'''

s = 0
cont = 0
while True:
    n = int(input('Digite um valor (Digite 999 para exibir a soma): '))
    if n == 999:
        break
    s = s + n
    cont += 1
print(f'A soma dos {cont} digitados foi: {s}.')