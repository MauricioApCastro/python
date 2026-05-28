
equipamentos = []

def cadastrar_equipamento():
    cliente = input("Nome do cliente: ")
    tipo = input("Tipo do equipamento: ")
    marca = input("Marca do equipamento: ")
    modelo = input("Modelo do equipamento: ")
    defeito = input("Defeito do equipamento: ")

    equipamento = {
        "cliente": cliente,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "defeito": defeito
    }
    return equipamento




def listar_equipamentos():
    print("\n=== Equipamentos cadastrados ===")

    for equipamento in equipamentos:
        print(f"cliente: {equipamento['cliente']} | Equipamento: {equipamento['equipamento']} | Defeito: {equipamento['defeito']} ")



    
while True:
    equipamento = cadastrar_equipamento()
    equipamento.append(equipamento)

    opcao = input("Cadastrar outro equipamento? (s/n): ").strip().lower()

    if opcao != "s":
        break

listar_equipamentos(equipamento)

    
    

   





    


    
    



    
    
    


