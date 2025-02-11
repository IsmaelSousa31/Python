v = int(input('Digite o valor do produto: '))

d = ""
z = 0
while d != "s" and d != "n":
    d = input('Você deseja desconto?:'))
    
    if d == "s":
        z = v / 10
        v = v - z
        print("O valor final do produto com desconto é: ", v)
        break
    elif d == "n":
        print("O valor final sem desconto é: ", v)
        break
    

    

    
    