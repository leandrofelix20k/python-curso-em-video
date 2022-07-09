#Desafio 20

#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import choices, shuffle

aluno1 = input('Digite seu nome: ')
aluno2 = input('Digite seu nome: ')
aluno3 = input('Digite seu nome: ')
aluno4 = input('Digite seu nome: ')

lista = aluno1, aluno2, aluno3, aluno4 

print(lista)