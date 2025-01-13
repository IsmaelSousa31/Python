def multiplicacao(x, y):
    print(f"{x=} y={y} = x * y = {x * y}")

multiplicacao(2, 10)

a = int(input("Digite um número para a ")) 
b = int(input("Digite um número para a ")) 

def multiplicacao(a, b):
    print("Multiplicação de a x b")
    print(f"{a=} x b={b} =  {a * b}")

multiplicacao(a, b)

"""
README

Descrição

Este é um exemplo básico de um programa em Python que realiza a multiplicação de dois números. O código inclui:

Uma função chamada multiplicacao para realizar a operação.

Um exemplo pré-definido para multiplicação.

A possibilidade de o usuário inserir seus próprios números para realizar a multiplicação.

Como usar

O código executa uma multiplicação inicial com os valores x = 2 e y = 10.

O usuário é solicitado a inserir dois números:

Digite um valor para a.

Digite um valor para b.

O programa calcula e exibe o resultado da multiplicação de a e b.

Exemplo de Saída

Multiplicação Inicial

x=2 y=10 = x * y = 20

Multiplicação com Entrada do Usuário

Se o usuário digitar 3 para a e 5 para b, a saída será:

Digite um número para a: 3
Digite um número para b: 5
Multiplicação de a x b
a=3 x b=5 = 15

Estrutura do Código

Definição inicial da função multiplicacao para valores fixos.

Leitura de entrada do usuário usando input().

Reimplementação da função multiplicacao para trabalhar com os valores fornecidos pelo usuário.

"""