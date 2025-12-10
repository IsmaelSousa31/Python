nome = input('Digite um nome: ')
novo_nome = ''
letra_atual = ''
i = 0

while i < len(nome):
    if i == 0:
        letra_atual = '*' + nome[i] + '*'
        novo_nome += letra_atual
        i += 1 
    elif i != ' ':
        letra_atual = nome[i] + '*'
        novo_nome += letra_atual
        i += 1 



print(novo_nome)


