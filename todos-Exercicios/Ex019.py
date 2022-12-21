#Um professor quer sortear um dos seus quatro alunos para apagar um quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

aluno1 = input('Digite seu nome: ')
aluno2 = input('Digite seu nome: ')
aluno3 = input('Digite seu nome: ')
aluno4 = input('Digite seu nome: ')

sorteado = choice([aluno1, aluno2, aluno3, aluno4])

print('O sorteado para limpar o quadro foi {}'.format(sorteado))
