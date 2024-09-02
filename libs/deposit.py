""" Depósitos """

def deposit():
    """ Faz depósitos """
    clear()

    global SALDO
    global EXTRATO

    while True:
        valor = input("\nInforme o valor do depósito: ")
        if valor.isdigit():
            valor = float(valor)
            break
        else:
            clear()
            print("Valor inválido!")

    if valor > 0:
        SALDO += valor
        EXTRATO += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepóstio de R${valor:.2f} realizado com sucesso.\n")

    else:
        print("\nOperação falhou! O valor informado é inválido.\n")

