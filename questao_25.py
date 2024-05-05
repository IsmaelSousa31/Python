depini = float(input("Digite o valor de depósito inicial: "))
txj = float(input('Digite a taxa de juros em %: '))

gjuros = 0
mes = int(0)
i = 0
totaljuros = 0

while(i < 24):
    gjuros = depini * (txj / 100)
    depini = depini + gjuros
    totaljuros = gjuros + totaljuros
    mes = mes + 1
    i = i + 1
    print(f"Mes {mes} Saldo R$ {depini:.2f} Juros R$ {gjuros:.2f}")

print(f'Total Ganho com juros: {totaljuros:.2f}')