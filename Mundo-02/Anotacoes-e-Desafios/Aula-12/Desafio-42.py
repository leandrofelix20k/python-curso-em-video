#Desafio 42

#Refaça o Desafio 035 dos triângulos, acrescentando o rescurso de mostrar que tipo de triângulo será formado
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    if(reta1 == (reta2 and reta3)):
        print('As três retas formam um triângulo Equilátero!')
    elif(reta1 == reta2 or reta2 == reta3):
        print('As três retas formam um triângulo Isósceles!')
    else:
        print('As três retas formam um triângulo Escaleno!')
else:
    print('As três retas não podem formar um triângulo')