#Desafio 95

'''
Aprimore o Desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''
jogador = {}
jogadores = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['gols'] = []
    jogador['total'] = 0
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}: ')))
        jogador['total'] = jogador['total'] + jogador['gols'][i]
    
    jogadores.append(jogador.copy())
    jogador.clear

    perg = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if perg == 'N':
        break

print('=-=' * 16)
print('{:<4}{:<10}{:>10}{:>17}'.format('cod|', 'nome', 'gols', 'total'))

for i in range(0, len(jogadores)):
    print(f' {i+1}', end= '  ')
    for k, v in jogadores[i].items():
        print('{:<16}'.format(str(v)), end= '')
    print()

print('--' * 22)
print('Digite -1 para sair do loop!')
while True:
    print('--' * 22)
    cod = int(input('Mostrar dados de qual jogador? '))
    if cod == -1:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[cod-1]["nome"]}')
    for j in range(0, len(jogadores[cod-1]['gols'])):
        print(f'No jogo {j+1} fez {jogadores[cod-1]["gols"][j]} gol(s)')
