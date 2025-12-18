"""
Exiba os indices da lista 

0 Maria
1 Helena
2 Luiz
3 Alice
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Alice')

n = 0

for nome in lista:
    print(n, nome)
    n = n + 1