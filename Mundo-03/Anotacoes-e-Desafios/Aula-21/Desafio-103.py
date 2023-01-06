#Desafio 103

'''
Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
que algum dado não tenha sido informado corretamente.
'''

def ficha(name='<desconhecido>', goals=0):
    if not name and not goals:
        print(f'O jogador <desconhecido> marcou 0 gols no campeonato.')
    elif not name:
        print(f'O jogador <desconhecido> marcou {goals} gols no campeonato.')
    elif not goals:
        print(f'O jogador {name} marcou 0 gols no campeonato.')
    else:
        print(f'O jogador {name} marcou {goals} gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome, gols)
#help(ficha)
