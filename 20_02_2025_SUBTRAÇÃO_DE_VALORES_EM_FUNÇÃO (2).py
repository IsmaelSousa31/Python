"Subtração com Parâmetro Opcional"

def subtrair(a, b, c = None):
    if c is not None:
        print(f"{a=} {b=} {c=}", a - b - c)
    else:
        print(f"{a=} {b=}", a - b)

subtrair(150, 40, 10)
subtrair(150, 10)
subtrair(120, 60)
subtrair(200, 10)