#Escreva um programa que leia um número inteiro qualquer e peça que para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

numInteiro = int(input('Digite um número inteiro: '))
print('''Escolha a base para a qual você deseja realizar a conversão:
1-Binário
2-Octal
3-Hexadecimal
*Digite um número diferente dos anteriores para converter para todas as bases!\n''')
baseConver = int(input('Resposta: '))
#Três formas:
binario = bin(numInteiro)
octal = format(numInteiro, "o")
hexadecimal = "{0:x}".format(numInteiro)

if(baseConver == 1):
    print('O número {} convertido para a base binária igual a {}'.format(numInteiro, binario[2:]))
elif(baseConver == 2):
    print('O número {} convertido para a base octal igual a {}'.format(numInteiro, octal))
elif(baseConver == 3):
    print('O número {} convertido para a base Hexadecimal igual a {}'.format(numInteiro, hexadecimal))
else:
    print('''\nO número {} em:
1-Binário= {}
2-Octal= {}
3-Hexadecimal= {}'''.format(numInteiro, binario[2:], octal, hexadecimal))
    