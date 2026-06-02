def cadastrar_equipamento():#pega os dados do usuário e armazena em variável
    cliente = input("Nome do cliente: ")
    tipo = input("Tipo do equipamento: ")
    marca = input("Marca do equipamento: ")
    modelo = input("Modelo do equipamento: ")
    defeito = input("Defeito do equipamento: ")

    cadastro = { #faz um dicionário com os dados
        "cliente": cliente,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito
    }

    return cadastro


def formatar_dados(cadastro): #decompõe o dicionário em variáveis e exibe formatado
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

def contar_por_marca(cadastros, marca_pesquisada):
    total = 0

    for cadastro in cadastros:
        if cadastro["marca"].lower() == marca_pesquisada.lower():
            total += 1

    return total

cadastros = [] #cria lista vazia

while True:
    novo_cadastro = cadastrar_equipamento()
    cadastros.append(novo_cadastro)

    opcao = input("Cadastrar outro equipamento? (s/n): ").strip().lower()

    if opcao != "s":
        break

listar_equipamentos(cadastros)

total_cadastros = contar_cadastros(cadastros)
print(f"\nTotal de equipamentos cadastrados: {total_cadastros}")
