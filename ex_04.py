nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
primeira_letra = nome[0]
ultima_letra = nome[-1]


if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")
    print("Seu nome tem ", len(nome)," letras")
    print(f"A primeira letra do seu nome é {primeira_letra}")
    print(f"A última letra do seu nome é {ultima_letra}")
else:
    print("Desculpe, você deixou campos vazios.")