#Desempacotamento de listas 

lista = ['Ola', 'Mundo', 1, 2, 3, 'Valores', 'Positivo']
#lista normal
print(lista)
#Print normal

#------
p, a, b, *_,  c = lista
print("Print com desempacotamento de lista: ", p, a, b)
#exibimos os primeiros valores da lsita pois foi armazenado assim p = 'Ola', a = 'Mundo' e b = 1

print(*_)
#Aqui exibimos os numeros apos inserirmos os valores de p, a, b
# *_ serve para armazena todos os valores finais em uma váriavel
#Nesse caso estamos exibindo somente até valores pois o valor 'Positivo' está armazenado em c