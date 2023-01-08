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
            return n
        else:
            print('\033[31mERRO! Digite um número válido\033[m')
    
    
numero = leiaInt('')
print(f'O valor {numero} é um inteiro!')