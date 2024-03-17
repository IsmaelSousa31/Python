Comparador de Valores em Python
Este é um simples programa em Python que compara dois valores inseridos pelo usuário e imprime uma mensagem indicando qual valor é maior.

Exemplo de Uso
python
Copy code
primeirovalor = input("Digite o primeiro valor ")
segundovalor = input("Digite o segundo valor ")

valor1 = int(primeirovalor)
valor2 = int(segundovalor)

if valor1 > valor2:
    print("O primeiro valor", valor1, "é maior que o segundo", valor2)
elif valor2 > valor1:
    print("O segundo valor", valor2, "é maior que o primeiro", valor1)
Saída
A saída do programa depende dos valores inseridos pelo usuário. Aqui estão dois exemplos:

Exemplo 1:
mathematica
Copy code
Digite o primeiro valor 5
Digite o segundo valor 3
O primeiro valor 5 é maior que o segundo 3
Exemplo 2:
mathematica
Copy code
Digite o primeiro valor 10
Digite o segundo valor 15
O segundo valor 15 é maior que o primeiro 10
Este programa é uma demonstração simples de como comparar valores em Python. Sinta-se à vontade para modificá-lo conforme necessário para atender às suas necessidades.