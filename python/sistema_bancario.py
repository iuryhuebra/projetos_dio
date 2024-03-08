menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Valor do depósito => "))

        if valor > 0:
            saldo += valor
            extrato += f"\n + R${valor:.2f}"
        else:
            print("Valor informado é inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor do saque => "))

            if valor > 0:

                if valor <= limite:

                    if valor <= saldo:
                        saldo -= valor
                        extrato += f"\n - R${valor:.2f}"
                        numero_saques += 1
                    
                    else:
                        print("Valor superior ao saldo disponível.")

                else:
                    print(f"Valor superior ao limite máximo de R${limite:.2f}")
            
            else:
                print("Valor informado é inválido.")

        else:
            print("Número máximo diários atingido.")

    elif opcao == "e":
        print("------------- EXTRATO -------------")

        if not extrato == "":
            print(f"{extrato}\n\nSaldo atual => R${saldo:.2f}")
        else:
            print("Extrato vazio.")

        print("-----------------------------------")
    elif opcao == "q":
        print("Sistema finalizado. Obrigado por utilizar o banco DIO!")
        break

    else:
        print("Favor escolher uma das opções descritas.")