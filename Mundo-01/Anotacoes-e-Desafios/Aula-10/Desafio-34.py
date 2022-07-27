#Desafio 34

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.

#Para salários superiores a R$1.250,00, calcule um aumento de 10%

#Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250.00:
    aumento = salario * 0.10
    print('Parabéns! Você recebeu um aumento de R${:.2f}, seu novo salário é de R${:.2f}'. format(aumento, salario+aumento))
else:
    aumento = salario * 0.15
    print('Parabéns! Você recebeu um aumento de R${:.2f}, seu novo salário é de R${:.2f}'. format(aumento, salario+aumento))
    