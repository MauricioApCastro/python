def cadastrar_equipamento():
    cliente = input("Nome do cliente: ")
    tipo = input("Tipo do equipamento: ")
    marca = input("Marca do equipamento: ")
    modelo = input("Modelo do equipamento: ")
    defeito = input("Defeito do equipamento: ")

    dados_equipamento = {
        "cliente": cliente,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito
    }

    return dados_equipamento


def listar_equipamentos(equipamentos):
    print("\n=== Equipamentos cadastrados ===")

    for equipamento in equipamentos:
        print(
            f"Cliente: {equipamento['cliente']} | "
            f"Equipamento: {equipamento['tipo']} {equipamento['marca']} {equipamento['modelo']} | "
            f"Defeito: {equipamento['defeito']}"
        )


equipamentos = []

while True:
    novo_equipamento = cadastrar_equipamento()
    equipamentos.append(novo_equipamento)

    opcao = input("Cadastrar outro equipamento? (s/n): ").strip().lower()

    if opcao != "s":
        break

listar_equipamentos(equipamentos)
