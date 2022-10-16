#Refaça o Desafio 009, mostrando a tabuada de um número que o úsuario escolher, só que agora utilizando um laço for.

num = int(input('Digite um número: '))
simb = '=' * 10

print('{} Tabuada do número {} {}'.format(simb, num, simb))

for i in range(1, 11, 1):
    print('\t{}x{} = {}'.format(num, i,  num * i))

print(simb * 4)
