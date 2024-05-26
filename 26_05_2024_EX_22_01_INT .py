primeirovalor = input("Digite o primeiro valor ")
segundovalor = input("Digite o segundo valor ")

valor1 = int(primeirovalor)
valor2 = int(segundovalor)

if valor1 > valor2:
    print("O primeiro valor", valor1, "é maior que o segundo ", valor2)
elif valor2 > valor1:
    print ("O segundo valor", valor2, "é maior que o primeiro", valor1)
