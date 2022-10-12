#Desafio 36

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Digite o valor da casa que você pretende financiar: '))
salario = float(input('Digite quanto você ganha atualmente: '))
tempo = int(input('Digite em quantos anos você vai pagar o empréstimo: '))
prestMensal = valorCasa / (tempo * 12) 

if(prestMensal > (salario * 0.30)):
    print('EMPRÉSTIMO NEGADO! VALOR DA PRESTAÇÃO MENSAL É SUPERIOR A 30% DO SEU ATUAL SALÁRIO!')
else:
    print('\nPARABÉNS! SEU EMPRÉSTIMO FOI APROVADO!')
    print('Você terá que pagar R${:.2f} pelos próximos {} meses'.format(prestMensal, tempo*12))