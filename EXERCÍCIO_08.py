#Exercicio: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.

#Resposta: 
salario  = float(input('Digite quanto você ganha por hora: '))
horat = float(input('Digite a quantidade de horas trabalhadas no mês: '))

saltot = salario * horat

ir = (saltot/100) * 11
inss = (saltot/100) * 8
sindicato = (saltot/100) * 5
sl = (((saltot - inss) - sindicato) - ir)

print(f' + Salario bruto: R${saltot:.2f}')
print(f'- ir (-11%): R${ir:.2f}')
print(f'- inss (-8%): R${inss:.2f}')
print(f'- sindicato (-5%): R${sindicato:.2f}')
print(f'- Salário Liquido: R${sl:.2f}')