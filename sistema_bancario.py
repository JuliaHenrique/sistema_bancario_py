menu = '''

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500 #limites de saque
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3 # limites de saques diarios

while True:


    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: r$ {valor:.2f}\n"

        else:
            print("O valor informado é invalido")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        

        if excedeu_saldo:
            print("Saldo insuficiente.")
        
        elif excedeu_limite:
            print("O valor de saque excede o limite permitido.")

        elif excedeu_saques:
            print("numero maximo de saques diarios excedido.") 

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: r${valor:.2f}\n"
            numero_saques += 1


        else:
            print('O valor informado é invalido')

    elif opcao == 'e':
        print('\nExtrato:')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == 'q':
        print('Obrigado por usar o sistema bancário!')
        break

  


   


