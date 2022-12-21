#Desafio 70

'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final,
mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000,00
C) Qual é o nome do produto mais barato
'''

cont = 1
produtosMaisMil = 0
total = 0

while True:
    print('=-' * 7)
    print(f' PRODUTO N°{cont}')
    print('=-' * 7)
    nomeProduto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: R$'))

    total = total + preco
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = nomeProduto
    if preco > 1000:
        produtosMaisMil += 1

    perg = str(input('Deseja adicionar mais produtos[S/N]? ')).upper()
    while perg != 'S' and perg != 'N':
        print('Opção Inválida')
        perg = str(input('Digite "S" para SIM e "N" para NÃO? ')).upper()
    if perg == 'N':
        break
    
    cont += 1

print('=-' * 14)
print('O total foi R${:.2f}'.format(total))
print(f'Produto(s) com valor superior a R$1000,00: {produtosMaisMil}')
print(f'Produto mais barato foi {produtoMaisBarato} que custou R${menorPreco}')
print('=-' * 14)