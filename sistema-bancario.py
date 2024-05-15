menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(saldo, valor, extrato):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato


def sacar():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo


# Lista de usuários e contas
usuarios = []
contas = []
numero_conta = 1

# Função para criar usuário (cliente)


def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remover caracteres não numéricos do CPF
    cpf = ''.join(c for c in cpf if c.isdigit())
    if any(user['cpf'] == cpf for user in usuarios):
        print("CPF já cadastrado.")
        return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento,
                    'cpf': cpf, 'endereco': endereco})

    # Função para criar conta corrente


def criar_conta(usuario):
    global numero_conta
    agencia = "001"
    numero_conta_global = numero_conta
    numero_conta += 1
    contas.append(
        {'agencia': agencia, 'numero_conta': numero_conta_global, 'usuario': usuario})


# Criar alguns usuários
criar_usuario("João", "01/01/1990", "123.456.789-00",
              "Rua A, 123 - Centro - São Paulo/SP")
criar_usuario("Maria", "15/05/1985", "987.654.321-00",
              "Av. B, 456 - Centro - Rio de Janeiro/RJ")

# Criar contas para os usuários
criar_conta("123.456.789-00")
criar_conta("987.654.321-00")

# Testar operações do sistema de controle financeiro
saldo, extrato = deposito(saldo=1000, valor=500, extrato="")
saldo, extrato = sacar()
saldo = extrato(saldo=saldo, extrato=extrato)

while True:
    opcao = input(menu_opcoes)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
