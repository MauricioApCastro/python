def mostrar_menu():
    print("\n=== Sistema de Equipamentos ===")
    print("1 - Cadastrar equipamento")
    print("2 - Listar todos")
    print("3 - Buscar por marca")
    print("4 - Buscar por cliente")
    print("5 - Mostrar total de cadastros")
    print("0 - Sair")


def cadastrar_equipamento():
    cliente = input("Nome do cliente: ")
    tipo = input("Tipo do equipamento: ")
    marca = input("Marca do equipamento: ")
    modelo = input("Modelo do equipamento: ")
    defeito = input("Defeito do equipamento: ")

    cadastro = {
        "cliente": cliente,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito
    }

    return cadastro


def formatar_dados(registro):
    cliente = registro["cliente"]
    tipo = registro["tipo"]
    marca = registro["marca"]
    modelo = registro["modelo"]
    defeito = registro["defeito"]

    texto = f"Cliente: {cliente} | Equipamento: {tipo} {marca} {modelo} | Defeito: {defeito}"

    return texto


def listar_equipamentos(cadastros):
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

    for item in cadastros:
        if item["marca"].strip().lower() == marca_pesquisada:
            texto = formatar_dados(item)
            print(texto)


def listar_por_cliente(cadastros, cliente_pesquisado):
    print(f"\n=== Equipamentos do cliente {cliente_pesquisado} ===")

    for item in cadastros:
        if item["cliente"].strip().lower() == cliente_pesquisado:
            texto = formatar_dados(item)
            print(texto)


def contar_por_cliente(cadastros, cliente_pesquisado):
    total_equipamentos = 0

    for item in cadastros:
        if item["cliente"].strip().lower() == cliente_pesquisado:
            total_equipamentos += 1

    return total_equipamentos


cadastros = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        novo_cadastro = cadastrar_equipamento()
        cadastros.append(novo_cadastro)
        print("Cadastro realizado com sucesso.")

    elif opcao == "2":
        listar_equipamentos(cadastros)

    elif opcao == "5":
        total_cadastros = contar_cadastros(cadastros)
        print(f"Total de equipamentos cadastrados: {total_cadastros}")

    elif opcao == "0":
        break

    else:
        print("Opcao invalida.")
