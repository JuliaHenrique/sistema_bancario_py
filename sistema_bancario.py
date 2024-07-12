import textwrap


def menu():
    menu = '''\m
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuario
    [q]\tSair
    => '''

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
            print("\n@@@ Saldo insuficiente. @@@")
        
    elif excedeu_limite:
            print("\n@@@ O valor de saque excede o limite permitido. @@@")

    elif excedeu_saques:
            print("\n@@@ numero maximo de saques diarios excedido. @@@") 

    elif valor > 0:
            saldo -= valor
            extrato += f"saque:\t\tr$ {valor:.2f}\n"
            numero_saques += 1
            print("\n@@@ Saque realizado com sucesso! @@@")

    else:
            print('O valor informado é invalido')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print("f\nSaldo:\t\tr$ {saldo:.2f:}")
    print("=============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n@@@ ja existe usuario com esse CPF: @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input(" Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe seu endereço(logradouro, nmr - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== usuario criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[e] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_conta(contas):
    for conta in contas:
        linha = f'''\
            agencia:\t{conta["agencia"]}
            c/c:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        '''

        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"


    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=limite_saques,
        )

    elif opcao == 'e':
       exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nu':
        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = lem(contas) + 1
        conta - criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 'lc':
        listar_conta(contas)

    elif opcao == 'q':
        print('Obrigado por usar o sistema bancário!')
        break
