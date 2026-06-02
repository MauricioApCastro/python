from armazenamento import carregar_cadastros, salvar_cadastros
from cadastros import (
    cadastrar_equipamento,
    contar_cadastros,
    contar_por_cliente,
    contar_por_marca,
    editar_cadastro,
    ler_campo_obrigatorio,
    listar_equipamentos,
    listar_por_cliente,
    listar_por_marca,
    remover_cadastro,
)
from menu import mostrar_menu


def calcular_proximo_id(cadastros):
    if len(cadastros) == 0:
        return 1

    maior_id = max(item["id"] for item in cadastros)
    return maior_id + 1


def main():
    cadastros = carregar_cadastros()
    proximo_id = calcular_proximo_id(cadastros)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            novo_cadastro = cadastrar_equipamento(proximo_id)
            cadastros.append(novo_cadastro)
            proximo_id += 1
            salvar_cadastros(cadastros)
            print("Cadastro realizado com sucesso.")

        elif opcao == "2":
            listar_equipamentos(cadastros)

        elif opcao == "3":
            if len(cadastros) == 0:
                print("Nenhum equipamento cadastrado.")
            else:
                marca_pesquisada = ler_campo_obrigatorio(
                    "Digite a marca para buscar/contar: "
                ).lower()

                total_marcas = contar_por_marca(cadastros, marca_pesquisada)
                print(
                    f"Total de equipamentos da marca {marca_pesquisada}: "
                    f"{total_marcas}"
                )

                listar_por_marca(cadastros, marca_pesquisada)

        elif opcao == "4":
            if len(cadastros) == 0:
                print("Nenhum equipamento cadastrado.")
            else:
                cliente_pesquisado = ler_campo_obrigatorio(
                    "Digite o nome do cliente: "
                ).lower()

                total_cliente = contar_por_cliente(cadastros, cliente_pesquisado)
                print(
                    f"Total de equipamentos do cliente {cliente_pesquisado}: "
                    f"{total_cliente}"
                )

                listar_por_cliente(cadastros, cliente_pesquisado)

        elif opcao == "5":
            total_cadastros = contar_cadastros(cadastros)

            if total_cadastros == 0:
                print("Nenhum equipamento cadastrado.")
            else:
                print(f"Total de equipamentos cadastrados: {total_cadastros}")

        elif opcao == "6":
            if len(cadastros) == 0:
                print("Nenhum equipamento cadastrado.")
            else:
                try:
                    id_pesquisado = int(input("Digite o ID para editar: "))

                    editado = editar_cadastro(cadastros, id_pesquisado)

                    if editado:
                        salvar_cadastros(cadastros)
                        print("Cadastro editado com sucesso.")
                    else:
                        print("Cadastro nao encontrado.")

                except ValueError:
                    print("ID invalido. Digite um numero.")

        elif opcao == "7":
            if len(cadastros) == 0:
                print("Nenhum equipamento cadastrado.")
            else:
                try:
                    id_pesquisado = int(input("Digite o ID para remover: "))

                    removido = remover_cadastro(cadastros, id_pesquisado)

                    if removido:
                        salvar_cadastros(cadastros)
                        print("Cadastro removido com sucesso.")
                    else:
                        print("Cadastro nao encontrado.")

                except ValueError:
                    print("ID invalido. Digite um numero.")

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
