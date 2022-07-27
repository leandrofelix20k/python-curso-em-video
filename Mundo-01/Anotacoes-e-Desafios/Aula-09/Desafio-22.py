#Desafio 22

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com tdoas minúsculas
#Quantas letras ao todo(sem considerar os espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
espacos = nome.count(' ')
lista = nome.split()

print('Seu nome em letras maiúsculas:', nome.strip().upper())
print('Seu nome em letras minúsculas:', nome.strip().lower())
print('Tamanho do seu nome:', len(nome) - espacos , 'letras')
print('Seu primeiro nome tem:', len(lista[0].strip()), 'letras')