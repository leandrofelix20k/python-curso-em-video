
#A redução de else if em python é elif

numero = int(input('Digite um número entre 0 e 10: '))

if(numero > 10 or numero < 0):
    print('O número digitado não está entre 0 e 10.')
elif(numero <= 5 and numero >= 0):
    print('O número digitado está entre 0 e 5.')
elif(numero > 5 and numero <= 10):
    print('O número digitado está entre 6 e 10.')
    