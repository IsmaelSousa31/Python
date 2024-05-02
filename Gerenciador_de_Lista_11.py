lista = []

while True:
    opcao = input('Selecione uma opção: [i]nserir, [a]pagar [l]istar: ')
    
    try:
        if opcao == 'i':
            valor = input('Valor: ')
            lista.append(valor)
        elif opcao == 'l':
            for indice, nome in enumerate(lista):
                print(indice, lista[indice])
        elif opcao == 'a':
            indices = input("Escolha o indice para apagar: " )
            
            try:
                indice = int(indices)
                del lista[indice]
            except ValueError:
                print('Valor digitado incorreto.')
                
    except:
        print('Valor digitado incorreto, tente novamente.')
        