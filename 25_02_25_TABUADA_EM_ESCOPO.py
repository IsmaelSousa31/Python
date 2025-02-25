print("Tabuada")
x = int(input("Digite um número para a tabuada: "))

def mais():
    i = 1
    print("Soma")
    while i <= 10:
        print(x, "+", i, "=", (x + i))
        
        
        
        i = i + 1
    
    print()
        
    def menos():   
        j = 1
        print("Subtração")
        while j <= 10:
            print(x, "-", j, "=", (x - j))
            
            
            
            j = j + 1
    
    menos()
    
    print()
    
    def divisao(): 
        c = float(0)
        k = 1
        print("Divisão")
        while k <= 10:
            c = x / k
            print(f"{x} / {k} = {c:.2f}")
            
            k = k + 1
    
    divisao()
    
    print()
    
    def multiplicacao():  
        
        m = 1
        print("Multiplicação")
        while m <= 10:
            print(x, "*", m, "=", (x * m))
            
            
            
            m = m + 1
    
    multiplicacao()
   
mais()

    