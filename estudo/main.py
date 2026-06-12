from menu import mostrar_menu
from ordens import cadastrar_ordem, contar_ordens, listar_ordens, listar_por_cliente, editar_OS, listar_por_status

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

    elif opcao == "3":
        cliente_pesquisado = input("Digite o nome do cliente: ").strip().lower()
        listar_por_cliente(ordens, cliente_pesquisado)
    
    elif opcao == "4":
        status = input("Digite o status: ").strip().lower()
        listar_por_status(ordens, status)
    
    elif opcao == "5":
        try:
            numero_id = int(input("Digite o número do ID: "))
            editado = editar_OS(ordens, numero_id)

            if editado:
                print("Ordem encontrada para edição.")
            else:
                print("Ordem não encontrada.")
        except ValueError:
            print("ID inválido. Digite um número.")

    elif opcao == "6":
        print("Remoção ainda não implementada.")




    elif opcao == "7":
        total = contar_ordens(ordens)
        print(f"Total de ordens: {total}")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
