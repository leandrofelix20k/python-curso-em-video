#Desafio 10

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

#Cotação atual = R$5,34

money = float(input('Quantos Reais você possui na carteira: '))

convertDol = money / 5.34

print('Com R${:.2f} você pode comprar US${:.2f}'.format(money, convertDol))