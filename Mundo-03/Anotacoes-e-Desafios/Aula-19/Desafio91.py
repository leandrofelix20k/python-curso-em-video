#Desafio 91

'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número no dado.
'''
from time import sleep
from random import randint

jogadores = {}

print('Valores sortedos: ')
for i in range(0, 4):
    dado = randint(1, 6)
    print(f'    {i+1}°jogador tirou {dado}')
    jogadores[f'jogador{i+1}'] = dado
    sleep(1)

cont = 1
print('Ranking dos jogadores: ')
for item in sorted(jogadores, key = jogadores.get, reverse= True):
    print(f'    {cont} Lugar: {item} com {jogadores[item]}')
    cont += 1
