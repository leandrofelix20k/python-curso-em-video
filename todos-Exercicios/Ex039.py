#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ela ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo do alistamento

#Seu programa também devera mostrar o tempo que falta ou que passou do prazo

import datetime

dataAtual = datetime.datetime.now()
data = dataAtual 
ano = data.strftime("%Y")
dataNasc = int(input('Digite o ano em que você nasceu: '))
idade = int(ano) - dataNasc

if(idade < 18):
    tempoRestante = 18 - idade
    print('''Calma lá rapaizinho! 
Você ainda não está no período para se alistar! 
Você poderá se alistar a partir do ano {}'''.format(int(ano) + tempoRestante))
elif(idade == 18):
    print('Vamo que vamo! Chegou a sua vez de se alistar!')
else:
    tempoAMais = idade - 18
    print('''Infelizmente já passou o tempo para você se alistar!
O ano que o senhor deveria ter se alistado foi em {}'''.format(int(ano) - tempoAMais))
