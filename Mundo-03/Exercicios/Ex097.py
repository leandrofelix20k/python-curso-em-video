'''
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro de mostre uma mensagem com tamanho
adptável.
'''

def msg(txt):
    print('-' * (len(txt) + 6))
    print(f'   {txt}')
    print('-' * (len(txt) + 6))


mensagem = str(input('Digite um texto qualquer: '))
msg(mensagem)
