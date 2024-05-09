frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(frase.strip())
    

print('Sem a utilização do strip:', lista_frases_cruas)

print('Com a utilização do strip:', lista_frases)
