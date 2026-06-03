from menu import mostrar_menu
from ordens import cadastrar_ordem, listar_ordens, contar_ordens


ordens = []
proximo_id = 1

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nova_ordem = cadastrar_ordem(proximo_id)
        ordens.append(nova_ordem)
        proximo_id += 1
        print("Ordem cadastrada com sucesso.")

    elif opcao == "2":
        listar_ordens(ordens)

    elif opcao == "7":
        total = contar_ordens(ordens)
        print(f"Total de ordens: {total}")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")