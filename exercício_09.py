listan = []
listav = []
conta = []
i = 0

print('Entradas')
while(i < 5):
    listanome = input('Digite o seu nome: ')
    listan.append(listanome)
    listavalor = input('Digite o seu saldo: R$ ')
    listav.append(listavalor)
    conta.append(i)
    i += 1

print('LISTA DE CLIENTES - BANCO NACIONAL')
print('NOME   SALDO  CONTA')

for i in range(len(listan)):
    print(f'{listan[i]: ^5} | {listav[i]: ^5} | {conta[i]: ^2}')

