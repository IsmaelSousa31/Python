"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    n = int( input("Digite um numero inteiro: "))

    n_tipo = type(n)

    if n_tipo == int:
        print('O número digitado é inteiro.')
        if n % 2 == 0:
            print("O número é par")
        else:
            print("O número é impar")
except:
    print('O número digitado não é inteiro. ')






