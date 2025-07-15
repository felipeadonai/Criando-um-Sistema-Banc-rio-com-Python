import textwrap
import time

def menu():
    menu = """\n
    ================ MENU ================
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\ttExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuario
    =>"""
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t R$ {valor:.2f}\n"
        print("...")
        time.sleep(1)
        print("\n=== Deposito realizado com sucesso! ===")
        time.sleep(1)
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Voce não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Numero maximo de saques excedeido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        time.sleep(1)
        print("\n Saque realizado com sucesso!")
        time.sleep(1)

    else:
        print("\n@@@Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n ============== EXTRATO ============== ")
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print('========================================')
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuario com esse CPF! @@@")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sila estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    time.sleep(1)
    print("==== Usuario criado com sucesso! ====")
    time.sleep(1)
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        time.sleep(1)
        print("\n==== Conta criada com sucesso! ===")
        time.sleep(1)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('='*50)
        print(textwrap.dedent(linha))
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

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            saldo,extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
main()