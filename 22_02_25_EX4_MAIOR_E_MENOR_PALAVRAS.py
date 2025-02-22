palavras = ["Python", "asimov", "código", "web", "Programação"]
n = 0
z = 0
maior = 0 
menor = 0
numero_palavras = 0
numero_palavras_m = 0

pos_maior = []
pos_menor = []

while n < len(palavras):
    numero_palavras += int(len(palavras[n]))
    
    if n == 0:
        pos_maior = palavras[n]
    elif n != 0 and numero_palavras > maior: 
        pos_maior = palavras[n]

    if numero_palavras > maior:
        maior = numero_palavras

    numero_palavras = 0
    n += 1

while z < len(palavras):
    numero_palavras_m += int(len(palavras[z]))

    if z == 0:
        pos_menor = palavras[z]
        menor = int(numero_palavras_m)
    elif z != 0 and numero_palavras_m < menor: 
        pos_menor = palavras[z]
        menor = int (numero_palavras_m)

    numero_palavras_m = 0
    z += 1


print(f"A maior palavra é {pos_maior} com {maior} letras") 
print(f"A menor palavra é {pos_menor} com {menor} letras") 