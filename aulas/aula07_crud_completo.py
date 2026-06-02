def mostrar_menu():
    print("\n=== Sistema de Equipamentos ===")
    print("1 - Cadastrar equipamento")
    print("2 - Listar todos")
    print("3 - Buscar por marca")
    print("4 - Buscar por cliente")
    print("5 - Mostrar total de cadastros")
    print("6 - Editar cadastro")
    print("7 - Remover cadastro")
    print("0 - Sair")


def ler_campo_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

        print("Campo obrigatorio. Digite um valor.")


def cadastrar_equipamento(proximo_id):
    cliente = ler_campo_obrigatorio("Nome do cliente: ")
    tipo = ler_campo_obrigatorio("Tipo do equipamento: ")
    marca = ler_campo_obrigatorio("Marca do equipamento: ")
    modelo = ler_campo_obrigatorio("Modelo do equipamento: ")
    defeito = ler_campo_obrigatorio("Defeito do equipamento: ")

    cadastro = {
        "id": proximo_id,
        "cliente": cliente,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito
    }

    return cadastro


def formatar_dados(registro):
    id_cadastro = registro["id"]
    cliente = registro["cliente"]
    tipo = registro["tipo"]
    marca = registro["marca"]
    modelo = registro["modelo"]
    defeito = registro["defeito"]

    texto = (
        f"ID: {id_cadastro} | "
        f"Cliente: {cliente} | "
        f"Equipamento: {tipo} {marca} {modelo} | "
        f"Defeito: {defeito}"
    )

    return texto


def listar_equipamentos(cadastros):
    if len(cadastros) == 0:
        print("Nenhum equipamento cadastrado.")
    else:
        print("\n=== Equipamentos cadastrados ===")

        for item in cadastros:
            texto = formatar_dados(item)
            print(texto)


def contar_cadastros(cadastros):
    total = len(cadastros)
    return total


def contar_por_marca(cadastros, marca_pesquisada):
    total_marcas = 0

    for item in cadastros:
        if item["marca"].strip().lower() == marca_pesquisada:
            total_marcas += 1

    return total_marcas


def listar_por_marca(cadastros, marca_pesquisada):
    print(f"\n=== Equipamentos da marca {marca_pesquisada} ===")

    encontrou = False

    for item in cadastros:
        if item["marca"].strip().lower() == marca_pesquisada:
            texto = formatar_dados(item)
            print(texto)
            encontrou = True

    if encontrou == False:
        print("Nenhum equipamento encontrado para essa marca.")


def contar_por_cliente(cadastros, cliente_pesquisado):
    total_equipamentos = 0

    for item in cadastros:
        if item["cliente"].strip().lower() == cliente_pesquisado:
            total_equipamentos += 1

    return total_equipamentos


def listar_por_cliente(cadastros, cliente_pesquisado):
    print(f"\n=== Equipamentos do cliente {cliente_pesquisado} ===")

    encontrou = False

    for item in cadastros:
        if item["cliente"].strip().lower() == cliente_pesquisado:
            texto = formatar_dados(item)
            print(texto)
            encontrou = True

    if encontrou == False:
        print("Nenhum equipamento encontrado para esse cliente.")


def remover_cadastro(cadastros, id_pesquisado):
    for item in cadastros:
        if item["id"] == id_pesquisado:
            cadastros.remove(item)
            return True

    return False


def editar_cadastro(cadastros, id_pesquisado):
    for item in cadastros:
        if item["id"] == id_pesquisado:
            item["cliente"] = ler_campo_obrigatorio("Novo nome do cliente: ")
            item["tipo"] = ler_campo_obrigatorio("Novo tipo do equipamento: ")
            item["marca"] = ler_campo_obrigatorio("Nova marca do equipamento: ")
            item["modelo"] = ler_campo_obrigatorio("Novo modelo do equipamento: ")
            item["defeito"] = ler_campo_obrigatorio("Novo defeito do equipamento: ")
            return True

    return False


cadastros = []
proximo_id = 1

while True:
    mostrar_menu()
    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        novo_cadastro = cadastrar_equipamento(proximo_id)
        cadastros.append(novo_cadastro)
        proximo_id += 1
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
            print(f"Total de equipamentos da marca {marca_pesquisada}: {total_marcas}")

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
