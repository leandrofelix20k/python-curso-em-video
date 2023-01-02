'''
Crie um programa que gerencia o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
'''

jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
jogador['gols'] = []
jogador['total'] = 0
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}: ')))
    jogador['total'] = jogador['total'] + jogador['gols'][i]
#jogador['total'] = sum(jogador['gols'])

print(jogador['total'])
print('=-' * 17)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('=-' * 17)
print(f'O jogado {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0, len(jogador['gols'])):
    print(f'    -Na partida {i+1}, fez {jogador["gols"][i]} gol(s)')
print(f'Fez um total de {jogador["total"]} gols.')
