#Dicionários

#Dicionários possuem índices literais. É possivel personalizar.

#Declaração:
dados = dict()
dados = {'nome':'Pedro', 'idade':25}

print(dados['nome'])
print(dados['idade'])

#print formatado:
print(f'Nome: {dados["nome"]}')
#*Deve-se utilizar aspas duplas para esse caso

#Adicionar elementos:
dados['sexo'] = 'F'
print(dados['sexo'])

#Remover elementos:
print(dados)
del dados['idade']
print(dados)

#Outra forma de declarar dicionários:
filme1 = {'titulo':'Interestelar',
        'ano':'2014',
        'diretor':'Christopher Nolan'
}
filme2 = {'titulo':'Matrix',
        'ano':'1999',
        'diretor':'Wachowski'
}
filme3 = {'titulo':'2001 - Uma Odisseia no Espaço',
        'ano':'1968',
        'direto':'Stanley Kubrick'
}

print('-='*20)
print(filme1['titulo'])

#Pegar apenas os valores:
print(filme1.values())

#Pegar as chaves:
print(filme1.keys())

#Pegar os dois
print(filme1.items())

print('-='*20)
for k, v in filme1.items():
    print(f'o {k} é {v}')

#Adicionar um dicionário em uma lista:
print('-='*20)
filmes = []
filmes.append(filme1)
filmes.append(filme2)
filmes.append(filme3)
print(filmes[2]['titulo'])

#Adicionado valores para um dicionário e colocando em uma lista:
estado = {}
brasil = []

print('-='*20)
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())   #Cria uma cópia do conteúdo

for c in brasil:
    for v in c.items():
        print(v)

