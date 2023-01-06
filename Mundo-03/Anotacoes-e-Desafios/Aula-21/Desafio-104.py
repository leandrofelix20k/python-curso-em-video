#Desafio 104

'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de
forma semelhante à função input() do python, só que fazendo a
validação para aceitar apenas um valor númerico.

EX:
n = leiaInt('Digite um valor númerico')
'''

def leiaInt(n):
    while True:
        n = input('Digite um número: ')

        if n.isnumeric():
            break
        else:
            print('ERRO! Digite um número válido')
    
    return n

    
numero = leiaInt('')
print(f'O valor {numero} é um inteiro!')