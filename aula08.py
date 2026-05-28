try:
    valor_pecas = float(input("Valor das peças: R$ "))
    valor_mao_obra = float(input("Valor da mão de obra: R$ "))
    total = valor_pecas + valor_mao_obra

    prioridade = input("Prioridade (baixa/média/alta): ").strip().lower()

    if prioridade not in ["baixa", "média", "media", "alta"]:
        print("Prioridade inválida.")
    else:
        if prioridade == "media":
            prioridade = "média"

        if total >= 1000:
            classificacao = "Orçamento crítico"
        elif total >= 500:
            classificacao = "Orçamento alto"
        else:
            classificacao = "Orçamento normal"

        if prioridade == "alta" and total >= 500:
            alerta = "Atenção: ordem prioritária com orçamento alto"
        else:
            alerta = "Sem alerta especial"

        print(f"Valor das peças: R$ {valor_pecas:.2f}")
        print(f"Valor da mão de obra: R$ {valor_mao_obra:.2f}")
        print(f"Total do orçamento: R$ {total:.2f}")
        print(f"Classificação: {classificacao}")
        print(f"Prioridade: {prioridade}")
        print(f"Alerta: {alerta}")

except ValueError:
    print("Erro: digite valores numéricos válidos.")