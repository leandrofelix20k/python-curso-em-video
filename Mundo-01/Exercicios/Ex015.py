#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carr custa R$60 por dia e R$o.15 por Km rodado.

km = int(input('Quantos Km você percorreu com o seu carro alugado? '))
dias = float(input('Por quantos dias você utilizou o carro? '))

precoTotal = (0.15 * km) + (60 * dias)

print('Você terá que pagar um total de R${:.2f}!'.format(precoTotal))