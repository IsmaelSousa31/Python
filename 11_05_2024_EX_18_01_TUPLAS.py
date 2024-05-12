gastosn = ("Agua","Luz","Gás","Mercado")
gastosint = (50,300,100,700)

g = len(gastosint)
valores_inteiros = 0

for i in range (g):
    valores_inteiros = valores_inteiros + gastosint[i]
    print(gastosn[i], gastosint[i])

print("A soma dos gastos totais  = ", valores_inteiros)