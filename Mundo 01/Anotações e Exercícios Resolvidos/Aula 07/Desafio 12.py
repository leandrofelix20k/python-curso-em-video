#Desafio 12

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precoProduto = float(input('Digite o preço do produto: '))

novoPreco = precoProduto - (precoProduto * 0.05)

print('O novo preço do seu produto, com uma desconto de 5% é de R${:.2f}'.format(novoPreco))