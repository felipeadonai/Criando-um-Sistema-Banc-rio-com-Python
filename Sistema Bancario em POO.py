import textwrap
import time

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500

    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("...")
            time.sleep(1)
            print("\n=== Depósito realizado com sucesso! ===")
            time.sleep(1)
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > Conta.LIMITE_VALOR_SAQUE
        excedeu_saques = self.numero_saques >= Conta.LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {Conta.LIMITE_VALOR_SAQUE:.2f}. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            time.sleep(1)
            print("\nSaque realizado com sucesso!")
            time.sleep(1)
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("=======================================")

class Banco:
    AGENCIA_PADRAO = "0001"

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe um usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ")

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)

        time.sleep(1)
        print("==== Usuário criado com sucesso! ====")
        time.sleep(1)

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if not usuario:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
            return None

        numero_conta = len(self.contas) + 1
        conta = Conta(Banco.AGENCIA_PADRAO, numero_conta, usuario)
        self.contas.append(conta)

        time.sleep(1)
        print("\n==== Conta criada com sucesso! ====")
        time.sleep(1)

    def listar_contas(self):
        if not self.contas:
            print("\nNenhuma conta cadastrada.")
            return

        for conta in self.contas:
            linha = f"""\
Agência:\t{conta.agencia}
C/C:\t\t{conta.numero_conta}
Titular:\t{conta.usuario.nome}
"""
            print("="*50)
            print(textwrap.dedent(linha))

    def encontrar_conta(self):
        numero_conta = int(input("Informe o número da conta: "))
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print("\n@@@ Conta não encontrada! @@@")
        return None

def menu():
    menu_texto = """\n
=============== MENU ===============
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova Conta
[nu]\tNovo Usuário
[lc]\tListar Contas
[q]\tSair
=> """
    return input(textwrap.dedent(menu_texto)).lower()

def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == 'd':
            conta = banco.encontrar_conta()
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)

        elif opcao == 's':
            conta = banco.encontrar_conta()
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)

        elif opcao == 'e':
            conta = banco.encontrar_conta()
            if conta:
                conta.exibir_extrato()

        elif opcao == 'nc':
            banco.criar_conta()

        elif opcao == 'nu':
            banco.criar_usuario()

        elif opcao == 'lc':
            banco.listar_contas()

        elif opcao == 'q':
            print("Encerrando o sistema...")
            break

        else:
            print("\nOpção inválida, tente novamente.")

if __name__ == "__main__":
    main()