#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro: '))
numero2 = int(input('Digite o primeiro: '))

if(numero1 > numero2):
    print('O primeiro valor digitado é maior que o segundo.')
elif(numero1 < numero2):
    print('O segundo valor digitado é maior que o Primeiro.')
else:
    print('Os valores são iguais.')
    