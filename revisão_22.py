m = [[10,10,10],[20,20,20],[30,30,30]]
q = [[10,10,10],[20,20,20],[30,30,30]]
soma = [[0,0,0],[0,0,0],[0,0,0]]

i = 0
j = 0

for i in range (3):
  for j in range (3):
    soma[i][j] = m[i][j] + q[i][j]

print(soma)


