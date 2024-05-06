# Dividir uma string em substrings com base em um caractere específico: (,) e retornar essas substrings em uma lista.
lista_de_compras = 'Arroz, Feijão, Macarrão, Açucar, Banana, Maça'
lista_com_virgula = lista_de_compras.split(',')
lista = []

for i, lista_de_compras in enumerate(lista_com_virgula):
    lista.append(lista_com_virgula[i].strip())
    
print(lista)
    