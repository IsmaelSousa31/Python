idade = int(input("Digite a sua idade: "))
numero_de_compras_no_mes = int(input("Digite a quantidade de compras no mês: "))

IDADE_MINIMA = 25 
COMPRAS_MINIMAS = 5 

jovem_ou_ativo = bool( idade <= 30 ) or (numero_de_compras_no_mes >= COMPRAS_MINIMAS)

elegivel_fidelidade = bool(idade > IDADE_MINIMA) and (numero_de_compras_no_mes >= COMPRAS_MINIMAS)

nao_elegivel_mas_jovem = bool(not elegivel_fidelidade) and (idade < IDADE_MINIMA)

print(f"Resultados")
print(f"Elegível Fidelidade (idade > 25 E compras >= 5): {elegivel_fidelidade}")
print(f"Jovem OU Ativo (idade <= 30 OU compras >= 5): {jovem_ou_ativo}")
print(f"NÃO Elegível, MAS Jovem (NOT Elegível E idade < 25): {nao_elegivel_mas_jovem}")