
menu = '''
 Seja bem-vindo a nosso banco,
 
 Escolha uma das opções abaixo: 
 
 [1] Deposito
 [2] Saque
 [3] Extrato
 [4] Sair
 
 Digite o numero da operação escolhida: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("\n\nDigite o valor a ser depositado: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
            print("""
---------------------------------
    Valor de R$ {:.2f} depositado!
---------------------------------\n""".format(valor))

        else:
            print("Operação falhou! O valor informado é invalido")

    elif opcao == "2":
        valor = float(input("Informe o valor de Saque: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n\nOperação falhou! Você não tem saldo disponível.\n\n")
        elif excedeu_limite:
            print("\n\nOperação falhou! Você excedeu o valor limite de saque.\n\n")
        elif excedeu_saques:
            print("\n\nOperação falhou! Voce excedeu seu limite de saques diario\n\n")
        else:
            print("""
---------------------------------
   Saque de R$ {:.2f} efetuado!
---------------------------------""".format(valor))
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R${valor:.2f}\n"

    elif opcao == "3":
        print("""
---------------------------------
{}
---------------------------------
        Saldo: R$ {:.2f}
---------------------------------\n""".format(extrato,saldo))

    elif opcao == "4":
        print("Muito obrigado por usar nossos serviços! Até logo.")
        break
    else:
        print("Operação Invalida! por favor selecione novamente a operação desejada.")

