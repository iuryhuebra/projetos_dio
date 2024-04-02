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
banco_usuarios = list()

def criar_usuario():

    global banco_usuarios
    
    print("-----------------------------------") 
    print("Para criação de usuário precisamos das seguintes informações: CPF, Nome, Data de Nascimento e Endereço.\nFavor informar dados abaixo:")
    cpf = verificar_cpf(banco_usuarios)

    if cpf != False:
        nome = input("Digite seu nome => ")
        data = input("Digite sua data de nascimento (Dia/Mês/Ano) => ")
        endereco = str(input("Digite seu endereço (Logadouro, Número - Bairro, Cidade/Estado Sigla) => "))
        registro = {"cpf":cpf, "nome":nome, "data":data, "endereco":endereco}
        banco_usuarios.append(registro)
        print("Usuário criado com sucesso.")
    

    elif cpf == False:
        print("")
    
    print("-----------------------------------") 
    
def verificar_cpf(): # Solicita o CPF, caso formato esteja incorreto modifica e verifica se CPF já consta na base.
    
    global banco_usuarios

    cpf = str(input("Digite seu CPF => "))
    duplicado = True

    while not cpf.isnumeric():
        
        cpf.replace(".", "").replace("-","")

        if not cpf.isnumeric():
            print("CPF inválido, digite novamente.")
            cpf = str(input("Digite seu CPF => "))

    # RESOLVER PROBLEMA DA VERIFICAÇÃO DO FORMATO INCLUINDO A VERIFICAÇÃO DA DUPLICIDADE

    return cpf


def saque(*, saldo, extrato, limite, numero_saques):

    global LIMITE_SAQUES

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
    
    return saldo, extrato, numero_saques


def deposito(saldo, extrato, /):

    valor = float(input("Valor do depósito => "))

    if valor > 0:
        saldo += valor
        extrato += f"\n + R${valor:.2f}"
    
    else:
        print("Valor informado é inválido.")
    
    return saldo, extrato

def consultar_extrato(saldo, / , *, extrato):

    print("------------- EXTRATO -------------")

    if not extrato == "":
        print(f"{extrato}\n\nSaldo atual => R${saldo:.2f}")
        
    else:
        print("Extrato vazio.")

    print("-----------------------------------")

while True:
    opcao = input(menu)
    
    if opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)

    elif opcao == "e":
        consultar_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Sistema finalizado. Obrigado por utilizar o banco DIO!")
        break

    else:
        print("Favor escolher uma das opções descritas.")