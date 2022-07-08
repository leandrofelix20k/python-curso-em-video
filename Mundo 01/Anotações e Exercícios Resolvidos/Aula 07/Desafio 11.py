#Desafio 11
 
#Crie um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

area = largura * altura

litrosTotal = area / 2

print('Será necessário {:.2f}l para pintar uma área de {}m²'.format(litrosTotal, area))