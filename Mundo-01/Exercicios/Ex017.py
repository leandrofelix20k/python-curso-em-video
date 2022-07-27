#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo , calcule e mostre o comprimento da hipotenusa

from math import hypot

catOposto = int(input('Digite o comprimento do cateto oposto: '))
catAdjacente = int(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(catOposto, catAdjacente)

print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))
