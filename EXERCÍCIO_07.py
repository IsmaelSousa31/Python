lista = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
i = 0
n = int(input('Digite um número: '))
r = 0
for i in lista:
    r = n * i[0]
    print(f'{n} x {i[0]} = {r}')
    