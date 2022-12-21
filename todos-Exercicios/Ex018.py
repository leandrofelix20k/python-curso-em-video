#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = int(input('Digite um ângulo qualquer: '))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))
