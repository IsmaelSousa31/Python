letra = input('Digite uma letra: ')

if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print('A letra digitada', letra, 'é uma vogal')
else:
    print('A letra digitada', letra, 'é uma consoante')