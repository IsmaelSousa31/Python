import math

def modelo_exponencial(C0, B, t):
    C = C0 * math.exp(B * t)
    return C

def main():
    try:
        C0 = float(input("Digite o número inicial de pessoas contaminadas (C0): "))
        B = float(input("Digite o número de pessoas que cada doente contamina por semana (B): "))
        t = float(input("Digite o tempo em semanas decorrido desde o primeiro caso (t): "))
        
        if C0 < 0 or B < 0 or t < 0:
            raise ValueError("Os parâmetros devem ser números positivos.")
        
        C = modelo_exponencial(C0, B, t)
        print(f"O número de pessoas contaminadas após {t} semanas é aproximadamente {C:.2f}.")
    
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
