#Verificador de CPF

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input("Digite o seu CPF: ")
#85520623058

lista = [int(digito) for digito in str(cpf)]

j = 10
i = 2
total = 0

for i in range (9):
   n = j * lista[i]
   total = total + n
   print(j,'*', lista[i], '= ', n)
   j = j - 1

print("Soma de todos os valores = ",total)
print()

print("Agora multiplicamos o valor por 10")
mtotal = total * 10
print(total, "* 10 =", mtotal)
print()

print('Agora dividimos o valor', mtotal, 'por 11')
restdivisao = mtotal % 11
print("Resultado =", restdivisao)
print("Se o resultado for maior que 9 o valor é 0")
print("Se o resultado for menor que 9 o valor é o valor da conta")

if (restdivisao > 9):
   print('Resultado é 0')
else:
   print("Resultado é o valor da conta", restdivisao)


lista = lista[:9]
lista.append(restdivisao)
print(lista)


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


print('Em busca do segundo digito')

v = 11
s = 0
ntotal = 0

for s in range (10):
    n = v * lista[s]
    ntotal = ntotal + n
    print(v,'*', lista[s], '= ', n)
    v = v - 1

print(ntotal)
ntotal = ntotal * 10
print("Multiplicao por 10 = ", ntotal)
ntotal = ntotal % 11
print("Dividindo por 11 = ", ntotal)

print("Resultado =", ntotal)
print("Se o resultado for maior que 9 o valor é 0")
print("Se o resultado for menor que 9 o valor é o valor da conta")

if (ntotal > 9):
   print('Resultado é 0')
else:
   print("Resultado é o valor da conta = ", ntotal)

lista.append(ntotal)

lista = [str(digito) for digito in lista]

# Une a lista de strings em uma única string
cpf2 = ''.join(lista)

print("CPF:", cpf2)

if(cpf == cpf):
   print("CPF é válido")
else:
   print("CPF inválido")