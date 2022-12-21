'''
Crie um programa que tenha uma tupla única com nomes de produtos e 
seus respectivos preços, na sequência.

No final, mostre uma listagem de preços organizando os dados em forma tabular
'''

produtos = ('Carne Bovina', 24.95, 'Frango', 19.99, 'Salsicha', 9.99,
        'Pizza', 16.86, 'Hambúrguer', 5.00, 'Peito de Peru', 28.45)

print('-' * 45)
print('{:-^45}'.format('Listagem dos Preços'))
print('-' * 45)

for i in range(0, len(produtos)):
    if type(produtos[i]) == str:
        print('{:.<35}'.format(produtos[i]), end= 'R$')
    else:
        print('{: 8.2f}'.format(produtos[i]))

print('-' * 45)
