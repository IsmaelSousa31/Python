palavra = input('Digite uma palavra: ')
verificador = ''
lenn = len(palavra)
lenn = -1 * lenn
i = -1

while i >= lenn:
    verificador = verificador + palavra[i]
    i = i + -1 

if(verificador == palavra):
    print(f'A palavra {verificador} é palíndromo')
else:
    print(f'A palavra não é palíndromo')