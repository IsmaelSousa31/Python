matriz1 = [[10],[9],[8],[10]]
matriz2 = [[10],[9],[8],[10]]

m = len(matriz1)
n = len(matriz1[0])

s = 0
j = 0
i = 0
total = 0


for i in range (m):
    for j in range (n):
        s = matriz1[i][j] + matriz2[i][j]
        total  = total + s
        print('Resultado da soma das matrizes = ', s)  
        
print('Resultado total da soma das matrizes = ', total)  