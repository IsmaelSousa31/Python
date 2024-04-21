nome = str(input('Digite o seu nome: '))
n = 0 
for j in range(len(nome)):
        n = n + 1

if(n <= 4):
    print('Seu nome é curto')
if(n == 5 or n == 6) :
    print('Seu nome é normal')
if(n > 6):
    print('Seu nome é muito grande')

