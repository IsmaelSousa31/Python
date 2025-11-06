def formatar_mensagem(texto):
    
    if texto.strip() == "":
        # Se for vazia ou só tiver espaços, retorna uma string vazia
        return ""
    
    remover_espaço_extras_texto = texto.strip()

    separar_palavras = remover_espaço_extras_texto.split()

    unir_palavras = " ".join(separar_palavras)

    palavras_minusculas = unir_palavras.lower()

  
    return palavras_minusculas


# Lê a mensagem enviada ao robô via input padrão
entrada = input() # Tipo de dado esperado: str


# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)
