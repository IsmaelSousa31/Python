m = [[10,10,10],[20,20,20],[30,30,30]]
i = 0
j = 0
n = 0
media = 0

for i in range (len(m)):
    for j in range (len(m)):
        media = m[i][j] + media
        n = n + 1
        
media = media / n
print(media)
