

def menu():
    menu = """\n
    ================ MENU ================
    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair
    => """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n==== Operação Cancelada! O valor informado é inválido. ====")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n==== Operação Cancelada! Você não tem saldo suficiente. ====")

    elif excedeu_limite:
        print("\n==== Operação Cancelada! O valor do saque excede o limite. ====")

    elif excedeu_saques:
        print("\n==== Operação Cancelada! Número máximo de saques excedido. ====")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n==== Operação Cancelada! O valor informado é inválido. ====")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
   

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual valor deseja depositar: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Qual valor deseja sacar: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione novamente a operação desejada.")


main()
