TAXA_FIXA = 0.15

dados_originais = [1, 2, 3]

dados_mutaveis = dados_originais

dados_copiados = dados_originais[:]

dados_mutaveis[0] = 99


print(f"dados_originais == dados_mutaveis | Resposta = {dados_originais == dados_mutaveis }")
print(f"dados_originais is dados_mutaveis | Resposta = {dados_originais is dados_mutaveis }")    
print(f"dados_originais == dados_copiados | Resposta = {dados_originais == dados_copiados }")    
print(f"dados_originais is not dados_copiados  | Resposta = {dados_originais is not dados_copiados  }")    
