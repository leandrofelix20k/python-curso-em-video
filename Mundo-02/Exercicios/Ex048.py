#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no instervalo de 1 até 500.

soma = 0

for i in range(1, 501, 1):
    if(i % 3 == 0):
        if(i % 2 != 0):
            soma += i
print('A soma de todo os número impares e múltiplos de 3, no intervalo de 1 até 500: {}'. format(soma))

#for i in range(1, 501, 2):
#    if(i % 3 == 0):
#        soma += i