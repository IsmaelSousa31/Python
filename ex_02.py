inventario = ["corda", "tocha", "espada"]

moedas = int(50)

moedas += 25

tupla = ("Amuleto", 1)

tem_tocha = "tocha" in inventario

nao_tem_pocao = "poção" not in inventario

r = tem_tocha + nao_tem_pocao

print(f"Total de moedas {moedas}")
print(f"Tem tocha no inventário ? R = {tem_tocha}")
print(f"Tem poção no inventário ? R = {nao_tem_pocao}")
print(f"Soma booleana R= {r}")