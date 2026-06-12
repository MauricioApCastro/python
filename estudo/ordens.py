def ler_campo_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

        print("Valor invalido. Digite novamente.")
        
def cadastrar_ordem(proximo_id):

    cliente = ler_campo_obrigatorio("Nome do cliente: ")
    telefone = ler_campo_obrigatorio("Telefone: ")
    equipamento = ler_campo_obrigatorio("Equipamento: ")
    marca = ler_campo_obrigatorio("Marca: ")
    modelo = ler_campo_obrigatorio("Modelo: ")
    defeito = ler_campo_obrigatorio("Defeito informado: ")

    status = "aberta"



    ordem = {
        "id": proximo_id,
        "cliente": cliente,
        "telefone": telefone,
        "equipamento": equipamento,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito,
        "status": status
    }

    return ordem

def formatar_ordem(ordem):

    
    texto = (
        f"ID: {ordem['id']} | "
        f"Cliente: {ordem['cliente']} | "
        f"Tel: {ordem['telefone']} | "
        f"Equipamento: {ordem['equipamento']} {ordem['marca']} {ordem['modelo']} | "
        f"Defeito: {ordem['defeito']} | "
        f"Status: {ordem['status']}"
    )

    return texto    

def listar_ordens(ordens):
    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
    else:
        for ordem in ordens:
            texto = formatar_ordem(ordem)
            print(texto)
    
def contar_ordens(ordens):
    total = len(ordens)
    return total
    
def listar_por_cliente(ordens, cliente_pesquisado):
    encontrou = False
    for ordem in ordens:
        if ordem['cliente'].strip().lower() == cliente_pesquisado:
            print (formatar_ordem(ordem))
            encontrou = True
        
    if encontrou == False:
        print("Nenhuma ordem encontrada para esse cliente")

def editar_OS(ordens, numero_id):
    for ordem in ordens:
        if ordem["id"] == numero_id:

            print (formatar_ordem(ordem))

            campo_escolhido = input("\n\nQual campo deseja alterar?:\n"
                    "1-cliente\n"
                    "2-telefone\n"
                    "3-equipamento\n"
                    "4-marca\n"
                    "5-modelo\n"
                    "6-defeito\n"
                    "7-status\n\n"
                )
            return True

    return False
            
def listar_por_status(ordens, status):    

    encontrou = False     
    for ordem in ordens:
        if ordem['status'].strip().lower() == status :
            print (formatar_ordem(ordem))
            encontrou = True
        
    if encontrou == False:
        print("Status não encontrado")
        encontrou = False



      
    
