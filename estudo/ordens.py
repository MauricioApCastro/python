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


    


        
    
    