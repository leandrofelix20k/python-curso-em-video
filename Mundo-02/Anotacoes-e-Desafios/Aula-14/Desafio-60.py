#Desafio 60

#Faça um programa que leia um número qualquer e mostre o seu fatorial

#Ex: 5! = 5x4x3x2x1 = 120

num = int((input('Digite um número: ')))
cont = num

print('{}!={}'.format(num, num), end='')
while num != 0:
    num -= 1
    if num != 0:
        cont = cont * num
        print('x{}'.format(num), end='')

print('=', cont)