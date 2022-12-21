#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

precoNormal = float(input('Digite o valor do produto que deseja comprar: R$'))
print('''Escolha a forma de pagamento:
1-À vista no dinheiro/cheque: 10% de desconto
2-À vista no cartão: 5% de cartão
3-Em até 2x no cartão: Preço Normal
4-3x ou mais no cartão: 20% de juros\n''')
condPagamento = int(input('Opção: '))

while(condPagamento < 1 or condPagamento >4):
    print('-' * 5, end= '')
    print('Opção Inválida! Digite Novamente!', end= '')
    print('-' * 5)
    print('''Escolha a forma de pagamento:
1-À vista no dinheiro/cheque: 10% de desconto
2-À vista no cartão: 5% de cartão
3-Em até 2x no cartão: Preço Normal
4-3x ou mais no cartão: 20% de juros\n''')
    condPagamento = int(input('Opção: '))

if(condPagamento == 1):
    precoFinal = precoNormal - (0.10 * precoNormal)
    print('Opção 1: Valor final do produto R${:.2f}'.format(precoFinal))
elif(condPagamento == 2):
    precoFinal = precoNormal - (0.05 * precoNormal)
    print('Opção 2: Valor final do produto R${:.2f}'.format(precoFinal))
elif(condPagamento == 3):
    print('Opção 3: 2 parcelas de R${:.2f}, SEM JUROS'.format(precoNormal/2))
else:
    precoFinal = precoNormal + (0.20 * precoNormal)
    parcelas = int(input('\nDigite em quantas parcelas deseja pagar: '))
    print('Opção 4: O produto ficou dividido em {} de R${:.2f}, COM JUROS'.format(parcelas, precoFinal/parcelas))
