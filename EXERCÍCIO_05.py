while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    c =  str(input('Digite o sinal que deseja da operação: '))
    v = 0
    
    if c == '*':
       v =  n1 * n2
       print(f'O resultado da multiplicação é {v}')
    elif c == '+':
       v =  n1 + n2
       print(f'O resultado da soma é {v}')
    elif c == '-':
       v =  n1 - n2
       print(f'O resultado da subtração é {v}')
    elif c == '/':
       v =  n1 / n2
       print(f'O resultado da divisão é {v}')
    
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    if sair == 's':
        break