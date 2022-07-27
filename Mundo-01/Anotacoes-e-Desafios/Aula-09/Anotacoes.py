frase = 'Curso em Vídeo Python'
print(frase)

#Fatiamento:

print('\nFatiamento de Strings:')
#Imprime apenas o caractere 9
print(frase[9])

#Imprime do caractere 9 até o 13
print(frase[9:13])

#Imprime do caractere 9 até o 120 pulando de duas em duas casas
print(frase[9:21:2])

#Ao omitir o ínicio, ele imprime do caractere 0 até o caractere após os dois pontos
print(frase[:5])

#Ao omitir o final, ele imprime do caractere anterior aos dois pontos até o último caractere
print(frase[15:])


#Análise:

print('\nAnálise de Strings:')
#Contar quantidade de caracteres e espaços
print(len(frase))

#Contar quantas vezes o caractere escolhido aparece na frase
print(frase.count('o'))

#Contar + Fatiamento
print(frase.count('o',0,13))

#Procurar strings na frase
print(frase.find('rso'))

#Ao colocar uma string que não existe na frase, ele retorna o valor -1
print(frase.find('Suco'))

#Operador 'in' para verificar se existe tal String dentro da frase. Retorna True ou False
print('Curso' in frase)
print('Suco' in frase)


#Transformação

#Alterar String

print('\nAlterar String:')
#Substituir String apenas no print
print(frase.replace('Curso', 'Suco'))
print(frase)

#Deixar toda a string em letras maiúsculas
print(frase.upper())

#Deixa a frase toda em maiúscula e conta quanta vezes o caractere 'O' aparece
print(frase.upper().count('O'))

#Deixar toda a string em letras minúsculas
print(frase.lower())

#Deixar todas os caracteres minúsculas e deixa o primeiro caratere em maiúsculas
print(frase.capitalize())

#Deixar os caracteres que iniciam as palavras em maiúsculas e os demais em minúsculas, levando em conta os espaços
print(frase.title())

#Remover todos os espaços antes e depois da frase
print(frase.strip())

#rstrip remove os espaços a direita da frase e lstrip remove os espaços a esquerda
print(frase.rstrip())
print(frase.lstrip())


#Divisão

print('\nDividir Strings: ')
#Cria uma divisão de acordo com os espaços
frase = frase.split()
print(frase)

#Junção

print('\nJuntar Strings: ')
#Junta as palavras
frase = ' '.join(frase)
print(frase)


#Uma string em seus micro-elementos é imutável, para alterar uma string, é necessário fazer uma atribuição atráves de funções


#Imprimir um texto:

print("""Mudança climática se refere a transformações de longo prazo nos 
padrões de temperatura e clima. Essas alterações podem ser naturais, 
mas desde o século 18 as atividades humanas têm sido a principal causa 
das mudanças climáticas, principalmente por causa da queima de 
combustíveis fósseis (como carvão, petróleo e gás), que produzem 
gases que retêm o calor.""")