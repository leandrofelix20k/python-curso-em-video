#Desafio 105 

'''
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as
seguinte informarções:

-Quantidade de notas
-A maior notas
-A menor nota
-A situação (opcional)

Adicione também a docstring da função
'''

def notas(*n, sit=False):
    """
    -> Função utilizada para analisar notas de uma turma.
    :parâmetro n: recebe as notas de uma turma.
    :parâmetro sit: é opcional. Indica se deve exibir a situação ou não.
    :return: Retorna um dicionário com os dados da turma.
    """
    turma = {}
    turma['total'] = len(n)

    for i in range(0, len(n)):
        if i == 0:
            turma['maior'] = n[i]
            turma['menor'] = n[i]
            turma['media'] = n[i] / len(n)
        else:
            if n[i] > turma['maior']:
                turma['maior'] = n[i]
            if n[i] < turma['menor']:
                turma['menor'] = n[i]
        turma['media'] = turma['media'] + n[i] / len(n)

    if sit:
        if turma['media'] < 5:
            turma['situação'] = 'RUIM'
        elif turma['media'] < 7:
            turma['situação'] = 'REGULAR'
        else:
            turma['situação'] = 'BOM'

    return turma



classe = notas(6, 8, 9.9, 6.7, 5.7, sit=True)
print(classe)

#help(notas)
