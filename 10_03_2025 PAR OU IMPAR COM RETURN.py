x = int(input("Digite um número: "))

def soma(a):
    if x % 2 == 0:
        return(f"O número {x} é par")
    else:
        return(f"O número {x} é impar")
    
print(soma(x))