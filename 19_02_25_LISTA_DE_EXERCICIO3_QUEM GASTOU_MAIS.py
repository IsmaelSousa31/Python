"10 Exercicios em pyhton"

"Exercício: quem gastou mais dinheiro?"

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

soma_joao = 0
soma_pedro = 0

for gastarjoao in gastos_joao:
    soma_joao += gastarjoao

for gastarpedro in gastos_pedro:
    soma_pedro += gastarpedro 
    
if soma_pedro > soma_joao:
    print("João foi o que mais gastou dos dois")
elif soma_joao > soma_pedro: 
    print("Pedro foi o que mais gastou dos dois")
else: 
    print("Os dois gastaram o mesmo valor")


