#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite seu atual salário: R$'))

novoSalario = salario + (salario * 0.15)

print('Seu novo salário com um aumento de 15%, é de R${:.2f}'.format(novoSalario))