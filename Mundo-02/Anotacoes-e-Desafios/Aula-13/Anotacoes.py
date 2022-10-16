#Estrutura de repetição for

print('Valor de i: ')
for i in range(1,10):
    print(i)

#range(10, 1, -1) - O último termo, é o intervaldor pelo qual a repetição vai ser percorrida

#Ex:
print('Valor do j: ')
for j in range(10, 1, -1):
    print(j)

#range com variáveis
n = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

print('Valor do j: ')
for k in range(n, n2):
    print(k)
