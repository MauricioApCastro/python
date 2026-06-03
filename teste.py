import sqlite3


ARQUIVO_BANCO = "equipamentos.db"


def conectar():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    return conexao


def criar_tabela(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT NOT NULL,
        tipo TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        defeito TEXT NOT NULL
    )
    """)


def cadastrar_equipamento(cursor):
    cliente = input("Nome do cliente: ").strip()
    tipo = input("Tipo do equipamento: ").strip()
    marca = input("Marca do equipamento: ").strip()
    modelo = input("Modelo do equipamento: ").strip()
    defeito = input("Defeito do equipamento: ").strip()

    cursor.execute("""
    INSERT INTO equipamentos (cliente, tipo, marca, modelo, defeito)
    VALUES (?, ?, ?, ?, ?)
    """, (cliente, tipo, marca, modelo, defeito))


def imprimir_equipamento(equipamento):
    print(
        f"ID: {equipamento[0]} | "
        f"Cliente: {equipamento[1]} | "
        f"Equipamento: {equipamento[2]} {equipamento[3]} {equipamento[4]} | "
        f"Defeito: {equipamento[5]}"
    )


def listar_equipamentos(cursor):
    cursor.execute("SELECT * FROM equipamentos")
    equipamentos = cursor.fetchall()

    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    print("\n=== Equipamentos cadastrados ===")

    for equipamento in equipamentos:
        imprimir_equipamento(equipamento)


def buscar_por_marca(cursor):
    marca_busca = input("Digite a marca para buscar: ").strip().lower()

    cursor.execute("""
    SELECT * FROM equipamentos
    WHERE lower(marca) = ?
    """, (marca_busca,))

    equipamentos = cursor.fetchall()

    if not equipamentos:
        print("Nenhum equipamento encontrado para essa marca.")
        return

    print(f"\n=== Equipamentos da marca {marca_busca} ===")

    for equipamento in equipamentos:
        imprimir_equipamento(equipamento)


def buscar_por_cliente(cursor):
    cliente_busca = input("Digite o cliente para buscar: ").strip().lower()

    cursor.execute("""
    SELECT * FROM equipamentos
    WHERE lower(cliente) = ?
    """, (cliente_busca,))

    equipamentos = cursor.fetchall()

    if not equipamentos:
        print("Nenhum equipamento encontrado para esse cliente.")
        return

    print(f"\n=== Equipamentos do cliente {cliente_busca} ===")

    for equipamento in equipamentos:
        imprimir_equipamento(equipamento)

def editar_por_id(cursor):
    id_busca = int(input("Digite o Id para editar:"))

    cliente = input("Novo nome do cliente: ").strip()
    tipo = input("Novo tipo do equipamento: ").strip()
    marca = input("Nova marca do equipamento: ").strip()
    modelo = input("Novo modelo do equipamento: ").strip()
    defeito = input("Novo defeito do equipamento: ").strip()

    cursor.execute("""
    UPDATE equipamentos
    SET cliente = ?, tipo = ?, marca = ?, modelo = ?, defeito = ?
    WHERE id = ?
    """, (cliente, tipo, marca, modelo, defeito, id_busca))

    if cursor.rowcount == 0:
        print("Nenhum equipamento encontrado com esse ID.")
    else:
        print("Equipamento atualizado com sucesso.")

def remover_por_id(cursor):
    try:
        id_busca = int(input("Digite o ID para remover: "))
    except ValueError:
        print("ID invalido. Digite um numero.")
        return

    cursor.execute("""
    DELETE FROM equipamentos
    WHERE id = ?
    """, (id_busca,))

    if cursor.rowcount == 0:
        print("Nenhum equipamento encontrado com esse ID.")
    else:
        print("Equipamento removido com sucesso.")

def mostrar_menu():

    print("\n=== Aula SQLite - Equipamentos ===")
    print("1 - Cadastrar equipamento")
    print("2 - Listar equipamentos")
    print("3 - Buscar por marca")
    print("4 - Buscar por cliente")
    print("5 - Editar por ID")
    print("6 - Remover por ID")
    print("0 - Sair")

def main():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela(cursor)
    conexao.commit()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_equipamento(cursor)
            conexao.commit()
            print("Equipamento cadastrado com sucesso.")

        elif opcao == "2":
            listar_equipamentos(cursor)

        elif opcao == "3":
            buscar_por_marca(cursor)

        elif opcao == "4":
            buscar_por_cliente(cursor)

        elif opcao == "5":
            editar_por_id(cursor)
            conexao.commit()
        
        elif opcao == "6":
            remover_por_id(cursor)
            conexao.commit()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opcao invalida.")

    conexao.close()


if __name__ == "__main__":
    main()
