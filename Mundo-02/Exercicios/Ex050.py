#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas saqueles que forem pares. Se o valor digitado for ímpar, desconsider-o.

print('Digite seis números inteiros:')
pares = 0
soma = 0

for i in range(0, 6):
    num = int(input())
    if(num % 2 == 0):
        soma += num
        pares += 1
    
print('A quantidade de números pares foi: {}\nA soma desses números pares é igual a: {}'.format(pares, soma))
        