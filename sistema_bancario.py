
def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado!")
        else:
            print("Operação falhou! Valor informado inválido.")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES ):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite máximo por saque excedido!")
        elif excedeu_saques:
            print("limite diário excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado!")
        else:
            print("Operação falhou! Valor informado inválido.")
        return saldo, extrato

def extrato_exibir (saldo, /, *, extrato):
        print("\n########## EXTRATO ##########")
        print("Nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#############################")

def novo_usuario(usuarios):
    cpf = input("informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuario com este CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, n - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário Criado!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "3":
            extrato_exibir(saldo, extrato=extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()