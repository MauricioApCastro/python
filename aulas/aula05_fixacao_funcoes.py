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


def formatar_dados(cadastro):
    cliente = cadastro["cliente"]
    tipo = cadastro["tipo"]
    marca = cadastro["marca"]
    modelo = cadastro["modelo"]
    defeito = cadastro["defeito"]

    texto = f"Cliente: {cliente} | Equipamento: {tipo} {marca} {modelo} | Defeito: {defeito}"

    return texto


def listar_equipamentos(cadastros):
    print("\n=== Equipamentos cadastrados ===")

    for cadastro in cadastros:
        texto = formatar_dados(cadastro)
        print(texto)


def contar_cadastros(cadastros):
    total = len(cadastros)
    return total


cadastros = []

while True:
    novo_cadastro = cadastrar_equipamento()
    cadastros.append(novo_cadastro)

    opcao = input("Cadastrar outro equipamento? (s/n): ").strip().lower()

    if opcao != "s":
        break

listar_equipamentos(cadastros)

total_cadastros = contar_cadastros(cadastros)
print(f"\nTotal de equipamentos cadastrados: {total_cadastros}")
