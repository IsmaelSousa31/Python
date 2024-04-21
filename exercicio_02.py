try:
    numero = int(input('Digite um numero inteiro '))
    print('O numero é inteiro')
    if(numero % 2 == 0):
        print(f'O numero {numero} é par')
    else:
        print('O numero é impar')

except ValueError:
    print('O numero não é do tipo inteiro')










