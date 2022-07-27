#Desafio 33

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input('Digite um número: ')) 
num2 = int(input('Digite outro número: ')) 
num3 = int(input('Digite mais um número: ')) 

maior = num1
menor = num1
#Maior
if num2 > num1:
    maior = num2
    if num3 > num2:
        maior = num3
elif num3 > num1:
    maior = num3
#Menor
if num2 < num1:
    menor = num2
    if num3 < num2:
        menor = num3
elif num3 < num1:
    menor = num3
    
print('O maior número é:', maior)
print('O menor número é:', menor)
