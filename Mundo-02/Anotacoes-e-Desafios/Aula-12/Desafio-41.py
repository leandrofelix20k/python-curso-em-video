#Desafio 41 

#A Confederação Nacional de Natação precisa de um rpograma que eleia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#Até 9 anos: MIRIM
#Até 14 ano: INFANTIL
#Até 19 ano: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

import datetime

dataAtual = datetime.datetime.now()
data = dataAtual 
ano = data.strftime("%Y")
dataNasc = int(input('Digite o ano em que você nasceu: '))
idade = int(ano) - dataNasc

if(idade <= 9):
    print('Categoria: MIRIM')
elif(idade <= 14):
    print('Categoria: INFANTIL')
elif(idade <= 19):
    print('Categoria: JUNIOR')
elif(idade <= 20):
    print('Categoria: SÊNIOR')
else: 
    print('Categoria: MASTER')
    