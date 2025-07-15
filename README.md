# 💰 Sistema Bancário em Python

Este projeto é um sistema bancário simples feito em Python, executado via terminal. Ele permite criar usuários e contas, realizar depósitos, saques e consultar extratos bancários, tudo controlado em memória com estruturas de dados básicas.

## 🚀 Funcionalidades

- Criar novo usuário (`nu`)
- Criar nova conta bancária (`nc`)
- Listar contas cadastradas (`lc`)
- Realizar depósitos (`d`)
- Realizar saques com limite de valor e número de operações por dia (`s`)
- Exibir extrato de transações (`e`)
- Encerrar o programa (`q`)

## 📋 Requisitos

- Python 3.7+

## ▶️ Como executar

1. Clone o repositório ou copie o código para um arquivo local:
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario-python.git
    cd sistema-bancario-python
    ```

2. Execute o script:
    ```bash
    python sistema_bancario.py
    ```

3. Use as opções do menu para interagir com o sistema.

## 🧠 Estrutura do Código

- `menu()` - Exibe as opções do sistema.
- `depositar()` - Realiza um depósito se o valor for positivo.
- `sacar()` - Realiza um saque com verificação de limite e saldo.
- `exibir_extrato()` - Mostra as movimentações financeiras e saldo atual.
- `criar_usuario()` - Cadastra um novo usuário com CPF único.
- `criar_conta()` - Associa uma conta a um usuário existente.
- `listar_contas()` - Exibe as contas cadastradas.
- `main()` - Loop principal de execução do programa.

## 🛡️ Regras de Negócio

- O saque está limitado a:
  - **3 saques diários**
  - **Valor máximo por saque: R$500,00**
- O CPF é usado como identificador único de usuário.
- O extrato mostra os depósitos e saques realizados.

## 📚 Tecnologias Utilizadas

- Python 3
- Módulos: `textwrap`, `time`

## ✍️ Autor

Desenvolvido por [Felipe Adonai].

---
