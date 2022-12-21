#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e
#todas as informações possíveis sobre ele

char = input('Digite alguma coisa: ')

print(type(char))
print('O caractere é um digito? {}\nO caractere é uma letra? {}\nO caractere é uma letra e/ou um número? {}\n'.format(char.isdigit(), char.isalpha(), char.isalnum(),))
