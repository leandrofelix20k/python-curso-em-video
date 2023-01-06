#Desafio 101

'''
Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nasicento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
ou OBRIGATÓRIO nas eleições.
'''

from datetime import date

def voto(n):
    situacaoVoto = ''
    if n < 16:
        situacaoVoto = (f'Com {n} anos:  NÃO VOTA!')
    elif n < 18:
        situacaoVoto = (f'Com {n} anos: VOTO OPCIONAL!')
    else:
        situacaoVoto = (f'Com {n} anos: VOTO OBRIGATÓRIO!')
    
    return situacaoVoto



anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de seu nascimento: '))
idade = anoAtual - anoNascimento

print(voto(idade))
