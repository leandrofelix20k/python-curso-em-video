'''
Crie uma tupla preenchida com os 20 primeiros colocados do 
Campeonato Brasileiro de Futebol, Na ordem de colocação.
Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense
'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 
        'Athletico-PR', 'São Paulo', 'Internacional', 
        'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 
        'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 
        'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-' * 30)
print('{:-^30}'.format('BRASILEIRÃO 2019'))
print('-' * 30)

print('=-=' * 10, '\nTabela:')
for i in range(0, 20):
    print('{}°{}'.format(i+1, times[i]))

print('=-=' * 10, '\nCinco Primeiros Colocados:')
for i in range(0, 5):
    print('{}°{}'.format(i+1, times[i]))

print('=-=' * 10, '\nQuatro Últimos Colocados:')
for j in range(16, 20):
    print('{}°{}'.format(j+1, times[j]))

print('=-=' * 10, '\nTimes em Ordem Alfabética: ')
ordemAlf = sorted(times)
for nomes in ordemAlf:
    print(nomes)

print('=-=' * 10, '\nO time da Chapecoense terminou o campeonato na {}°Posição'.format(times.index('Chapecoense') + 1))
