def identificar_categoria_gadget(codigo):
    """
    Recebe uma string 'codigo' e retorna a categoria associada:
    - 'T': tablet
    - 'P': phone
    - 'N': notebook
    Se não corresponder, retorna 'unknown'.
    """
    
    if(codigo[0] == "T" or codigo[0] == "t"):
        return "tablet"
    elif(codigo[0] == "P" or codigo[0] == "p"):
        return "phone"
    elif(codigo[0] == "N" or codigo[0] == "n"):
        return "notebook"
    else:
        return "unknown"

 

# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'