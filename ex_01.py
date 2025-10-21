valor_original = float(input("Digite um número: "))

valor_inteiro = int(valor_original)
valor_texto = str(valor_original)

quociente = valor_inteiro // 3 

print(f"Valor original = {valor_original} tipo {type(valor_original)}")
print(f"Valor inteiro = {valor_inteiro} tipo {type(valor_inteiro)}")
print(f"Valor em texto = {valor_texto} tipo {type(valor_texto)}")
print(f"Valor quociente = {quociente} tipo {type(quociente)}")
