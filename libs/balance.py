""" Extrato """

def balance():
    """ Exibe extrato """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
    print(f"\nSALDO: R$ {SALDO:.2f}")
    print("==========================================")

    input("Pressione uma tecla para continuar...\n")
    clear()

