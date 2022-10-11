#Desafio 44

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

precoNormal = float(input('Digite o valor do produto que deseja comprar: '))
condPagamento = int(input('Escolha a forma de pagamento: \n1-À vista no dinheiro/cheque: 10% de desconto\n2-À vista no cartão: 5% de cartão\n3-Em até 2x no cartão: Preço Normal\n4-3x ou mais no cartão: 20% de juros\n'))

while(condPagamento < 1 or condPagamento >4):
    print('-' * 5, end= '')
    print('Opção Inválida! Digite Novamente!', end= '')
    print('-' * 5)
    condPagamento = int(input('\nEscolha a forma de pagamento: \n1-À vista no dinheiro/cheque: 10% de desconto\n2-À vista no cartão: 5% de cartão\n3-Em até 2x no cartão: Preço Normal\n4-3x ou mais no cartão: 20% de juros\nEscolha: \n'))

if(condPagamento == 1):
    precoFinal = precoNormal - (0.10 * precoNormal)
    print('Opção 1: Valor final do produto R${:.2f}'.format(precoFinal))
elif(condPagamento == 2):
    precoFinal = precoNormal - (0.05 * precoNormal)
    print('Opção 2: Valor final do produto R${:.2f}'.format(precoFinal))
elif(condPagamento == 3):
    print('Opção 2: Valor final do produto R${:.2f}'.format(precoNormal))
else:
    precoFinal = precoNormal + (0.20 * precoNormal)
    print('Bad Escolha! Opção 4: Valor final do produto R${:.2f}'.format(precoFinal))

