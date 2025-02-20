"somando 3 valores em funções"

def soma(x, y, z = None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)
    
soma(20, 10)
soma(20, 10, 50)
soma(20, 10, 60)
soma(20, 10, 0)