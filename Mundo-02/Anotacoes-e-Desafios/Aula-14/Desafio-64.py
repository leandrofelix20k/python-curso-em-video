#Desafio 64

#Crie um programa que leia vários números inteiros pelo teclado.O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quanto números foram digitados e qual foi a soma entre eles(desconsiderando o flag)

print('Para interromper o laço, digite 999 a qualquer momento')
print('Digite quais números dejesa fazer a soma: ')

numeros = int(input())

cont = 0
soma = 0
while numeros != 999:
    soma = soma + numeros
    cont += 1
    numeros = int(input())
print('Você digitou {} número(s). A soma do(s) número(s) digitado(s) é igual {}'.format(cont, soma))