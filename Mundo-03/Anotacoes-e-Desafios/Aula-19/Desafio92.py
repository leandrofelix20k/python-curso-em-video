#Desafio 92

'''
Crie um programa que leia nome, ano de nascimento, e carteira de
trabalho e cadastre-os(com idade) em um dicionário se por acaso a 
CTPS for diferente de zero, o dicionário receberá também o ano de
contratação e o salário. calcule e acrescente, além além da idade,
com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

dadoPrevidencia = {}
anoAtual = date.today().year

dadoPrevidencia['nome'] = str(input('Nome: '))
dadoPrevidencia['idade'] = (anoAtual - int(input('Ano de Nascimento: ')))
dadoPrevidencia['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))

if dadoPrevidencia['ctps'] == 0:
    print('-=' * 15)
    for k, v in dadoPrevidencia.items():
        print(f'{k}: {v}')
else:
    dadoPrevidencia['contratação'] = int(input('Ano de contratação: '))
    dadoPrevidencia['salário'] = float(input('Salário: R$ '))
    dadoPrevidencia['aposentadoria'] = (dadoPrevidencia['contratação'] + 35) - (anoAtual - dadoPrevidencia['idade'])

    print('-=' * 15)
    for k, v in dadoPrevidencia.items():
        print(f'{k}: {v}')
