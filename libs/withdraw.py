""" Saques """

def withdraw():
    """ Faz saques """
    global SALDO
    global EXTRATO
    global NUMERO_SAQUES

    while True:
        valor = input("\nInforme o valor do saque: ")
        if valor.isdigit():
            valor = float(valor)
            break
        else:
            clear()
            print("\nValor inválido!")

    excedeu_saldo = valor > SALDO

    excedeu_limite = valor > LIMITE

    excedeu_saques = NUMERO_SAQUES >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        SALDO -= valor
        EXTRATO += f"Saque: R$ {valor:.2f}\n"
        NUMERO_SAQUES += 1
        print(f"\nSaque no valor de R${valor:.2f} realizado com sucesso.\n")


    else:
        print("\nOperação falhou! O valor informado é inválido.")

