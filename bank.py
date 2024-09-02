""" Sample bank routine """
from libs.deposit import deposit
from libs.withdraw import withdraw
from libs.balance import balance


import os
import datetime

def clear():
    """Clear terminal"""

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def greeting():
    """ Message based on timedate """
    time = datetime.datetime.now()
    hour = time.strftime('%H')
    if  int(hour, 10) < 12:
        print("Bom dia!")
    elif int(hour, 10) >= 12 and int(hour, 10) <= 18:
        print("Boa Tarde!")
    else:
        print("Boa Noite!")



MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

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



def balance():
    """ Exibe extrato """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
    print(f"\nSALDO: R$ {SALDO:.2f}")
    print("==========================================")

    input("Pressione uma tecla para continuar...\n")
    clear()


#Menu principal começa aqui

clear()
greeting()


while True:
    print("Por favor, escolha uma opção:")

    opcao = input(MENU)

    if opcao == "d":

        clear()
        deposit()

    elif opcao == "s":
        clear()
        withdraw()

    elif opcao == "e":

        clear()
        balance()

    elif opcao == "q":
        break

    else:
        clear()
        print("Operação inválida, por favor selecione novamente a operação desejada.")


print("\nAté a próxima!")
