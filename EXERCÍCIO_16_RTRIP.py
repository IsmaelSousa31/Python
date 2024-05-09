frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(frase.rstrip())
    
print('Sem a utilização do rstrip:', lista_frases_cruas)

print('Com a utilização do rstrip:', lista_frases)