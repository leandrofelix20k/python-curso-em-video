#Tratamento de Erros e Exceções

#Comando para exceções
'''
try:
    operação
except:
    falha
'''

try: #Tente rodar esse trecho de código
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except: #Caso não dê certo, faça isso.
    print(f'Problema encontrado foi {TypeError.__class__}') #Exbi o erro para o usuário
else: #Caso dê certo, faça isso.
    print(f'Resultado: {r:.2f}')
finally:
    print('Volte Sempre!')

#Os comandos else e finally são opcionais

print('-' * 14)
try:
    b = int(input('Digite a base do retângulo: '))
    h = int(input('Digite a altura do retângulo: '))
    area = a * b
except Exception as erro: #Caso a exceção for um erro
    print(f'Problema encontrado foi {erro.__class__}') #Imprima a classe do erro
else: 
    print(f'Área: {area:.2f}')
finally:
    print('Volte Sempre!')

#É possível criar vários exceptions para diferentes tipos de erros

'''
try:
    b = int(input('Digite a base do retângulo: '))
    h = int(input('Digite a altura do retângulo: '))
    area = a * b
except TypeError: 
    print(''x)
except ValueError: 
    print(''x)
except OSEerror: 
    print(''x)
except (AttributeError, KeyboardInterrupt)
'''