nome = input('Digite seu nome ')
idade = input('Digite sua idade ')
i = 0
j = 0
n = 0

if((nome != "") and (idade != "")):
    print(f"seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    while i < len(nome):
        letra = nome[i]
        if letra == ' ':
            print('Seu nome contém espaços')
            break
        i += 1
    else:
        print('Seu nome não contém espaços')

    for j in range(len(nome)):
        if nome[j] == ' ':
           continue
        n = n + 1

    print(f'Seu nome tem {n} Letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
elif(nome == "") and (idade == ""):
    print('Desculpe, você deixou campos vazios')

    