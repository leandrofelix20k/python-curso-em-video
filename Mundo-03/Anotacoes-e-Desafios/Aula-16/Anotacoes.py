#Tuplas:

#Tuplas são variáveis compostos que podem armazenar vários valores

lanche = ('Pizza', 'Refri', 'Ketchup')
print(lanche)

#Também é possivél criar uma tupla sem a utilização de parênteses

lunch = 'Guacamole', 'Frijol', 'Suco'
print(lunch)

print(lanche[1])
print(lanche[-1])

#São imúltaveis:
#lanche[1] = 'Cerveja'

for i in lanche:
    print(f'O lanche será {i}')

print(sorted(lanche))

t1 = (1, 4, 3, 2)
t2 = (7, 5, 6, 5)
t3 = t1 + t2
print(t3)
#Ordena os valores
print(sorted(t3))
#Conta quantos vezes o valor 5 aparece na tupla
print(t3.count(5))
#Pega a primeira ocorrência de determinado valor
print(t3.index(5))
#É possível misturar diferente tipos em uma só tupla
pessoa = ('Leandro', 25, 'M', 'Solteiro')
print(pessoa)
#Deletar uma tupla:
del(pessoa)
