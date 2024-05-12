nome = ('João', 'Maria', 'Alfredo', 'Joana')
idade = (15,16,15,16)
nota = (10,10,5,4)

idadem = 0
mediam = 0

g = int(len(nome))
valores_inteiros = 0

for i in range (g):
    idadem = idadem + idade[i]
    mediam = mediam + nota[i]
    print('Nome', nome[i],'Idade', idade[i],'Nota', nota[i])

idadem = float(idadem / g)
mediam = float(mediam / g)

print(f"A média de idade dos estudantes  = {idadem:.1f}")
print(f'A média das notas dos estudantes  = {mediam:.1f}')