#Operações aritméticas
adicao = 3 + 3 #6
subtracao = 5 - 2 #3
multiplicacao = 3 * 5 # 15
divisao = 15 / 4 #3.75
potencia = 2 ** 3 #8
divisaoInteira = 15 // 4 #3
restoDivisao = 4 % 3 #1

#Forma de imprimir:

nome = input()
#alinhado a direita
print('Olá {:>20}, prazer em conhece-lo'.format(nome))
#alinhado a esquerda
print('Olá {:<20}, prazer em conhece-lo'.format(nome))
#alinhado ao centro
print('Olá {:^20}, prazer em conhece-lo'.format(nome))
#alinhado ao centro e com sinais de igualdade
print('Olá {:=^20}, prazer em conhece-lo'.format(nome))

#Quebra de linha

print('255\n255')
#\n quebra a linha
print('255', end='' + '255')
#end='' junta a linha