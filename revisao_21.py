m = [[10,20,30000],[5000,1,60],[10,180,30]]
i = 0
j = 0
maior = 0

for i in range (3):
    for j in range (3):
        if(maior < m[i][j]):
            maior = m[i][j]

print('O maior numero da matriz  = ', maior)
    