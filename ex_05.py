senha = input("Digite sua senha: ")

tem_maiuscula = int(0)
tem_minuscula = int(0)
tem_numero = int(0)
tem_simbolo = int(0)
tipos_diferentes = int(0)


for letra in senha:
  
    if letra.isupper():
        
        tem_maiuscula += 1 
    elif letra.islower():
        tem_minuscula += 1 
        
    elif letra.isdigit():
        tem_numero += 1
      
    else:
        tem_simbolo += 1
        
tipos_diferentes = 0
if tem_maiuscula > 0:
    tipos_diferentes += 1
if tem_minuscula > 0:
    tipos_diferentes += 1
if tem_numero > 0:
    tipos_diferentes += 1
if tem_simbolo > 0:
    tipos_diferentes += 1

comprimento_minimo = int(8)
verificação_de_força = str("") 

quantidade_de_letras = len(senha)

if quantidade_de_letras < comprimento_minimo:
    verificação_de_força = "FRACA"
elif quantidade_de_letras >= comprimento_minimo and tipos_diferentes >= 3:
    verificação_de_força = "FORTE" 
elif quantidade_de_letras >= comprimento_minimo and tipos_diferentes >= 2:
    verificação_de_força = "MODERADA"

mensagem = f"""
    ========== Resultado da Análise ==========
    Verificação de força = {verificação_de_força}
    Quantidade de Maiusculas = {tem_maiuscula}
    Quantidade de Minusculas = {tem_minuscula}
    Quantidade de Números = {tem_numero}
    Quantidade de Simbolos = {tem_simbolo}
    Quantidade de Letras = {quantidade_de_letras}
    ==========================================
"""

print(mensagem)