#Modularização

'''
A modularização, tem por objetivo, dividir um programa grande em
partes menores, a fim de tornar mais fácil a manutenção e a
legibilidade do código.
'''

#Vantagens:
'''
- Organização do código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos
'''

#Para fazer a ligação entre o arquivo das funções e seu programa principal:
import funcoes 

num = int(input('Digite um número: '))

#Chamando uma função específica:

numParOuImpar = funcoes.parOuImpar(num)
fat = funcoes.fatorial(num)

print(f'O número {num} é {numParOuImpar}')
print(f'O fatorial de {num} é {fat}')

'''
Para criar pacotes para as funções, é necessário criar várias pastas
dentro de uma pasta que irá armazenar todas as funções

Ex:
    funcoes
        cores
        datas
        números
        strings
'''

