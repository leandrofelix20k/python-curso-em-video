#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura

litrosTotal = area / 2

print('Será necessário {:.2f}l de tinta para pintar uma parede de dimensão de {:.2f}x{:.2f}, com uma área de {:.2f}m²'.format(litrosTotal, largura, altura, area))