'''
Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nasicento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
ou OBRIGATÓRIO nas eleições.
'''

def voto(n):
    #Importar uma biblioteca dentro de uma função economiza memória, mas só poderá ser utilizada dentro da função
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - n
    situacaoVoto = ''
    if idade < 16:
        situacaoVoto = (f'Com {idade} anos:  NÃO VOTA!')
    elif idade < 18 or idade > 65:
        situacaoVoto = (f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        situacaoVoto = (f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    
    return situacaoVoto


anoNascimento = int(input('Digite o ano de seu nascimento: '))

print(voto(anoNascimento))
