soma = 0

for i in range(1, 500, 1):
    if(i % 3 == 0):
        if(i % 2 != 0):
            print(i)
            soma += i
print('A soma de todo os número impares e múltiplos de 3, no intervalo de 1 até 500: {}'. format(soma))
