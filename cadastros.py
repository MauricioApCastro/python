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
