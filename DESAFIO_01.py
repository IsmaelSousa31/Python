menu = """
[c] Criar Usúario
[cc] Criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -=  valor
        
        extrato += f"Saque: R$ {valor:.2f}\n"

        numero_saques += 1

        return saldo, extrato, numero_saques
        

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def deposito(saldo, extrato, valor, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato_(saldo , /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = str(input("Digite o CPF (sem traços e pontos): "))
    usuario_existente = filtrar_usuario(cpf, usuarios)
    if usuario_existente:
        print("CPF já existe!")
        return
    else:
        nome = str(input("Digite o nome: "))
        data_nascimento = str(input("Digite o data de nascimento: "))
        endereco = str(input("Digite o endereço [logradouro, nro - bairro - cidade/sigla]: "))
    
        novo_usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}

        usuarios.append(novo_usuario)
        print("Usuário criado com sucesso!")

def criar_conta(contas, usuarios):
    cpf = str(input("Informe o CPF do usuário (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        numero_conta = len(contas) + 1

        nova_conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

        contas.append(nova_conta)

        print(f"Conta número {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")
    else:
        print("Erro! Usuário não encontrado. Crie o usuário antes de criar uma conta.")
        return


usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:

    opcao = input(menu)

    if opcao == "c":
        criar_usuario(usuarios)

    elif opcao == "cc":
        criar_conta(contas, usuarios)
        

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, extrato, valor, )


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        extrato_(saldo, extrato= extrato)

        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")