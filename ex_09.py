n = True

while n:
    try:
        print(' 1 - Soma')
        print(' 2 - Subtração')
        print(' 3 - Multiplicação')
        print(' 4 - Divisão')
        print(' 5 - Sair')
        operador = int( input('Digite um número para escolher o operador lógico que deseja utilizar:'))
    
   
        if operador == 1:
            primeiro_numero = int(input('Digite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            print(f'A soma de {primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}')
        elif operador == 2:
            primeiro_numero = int(input('Digite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            print(f'A subtração de {primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}')
        elif operador == 3:
            primeiro_numero = int(input('Digite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            print(f'A multiplicação de {primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero} ')
        elif operador == 4:
            primeiro_numero = int(input('Digite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            print(f'A divisão de {primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero} ')
        elif operador == 5:
            n = False
            print('Saindo...')
    except:
        print('Você não digitou um operador inválido.')