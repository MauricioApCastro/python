ordem_valida = 0
soma_total = 0
soma_critica = 0
orcamentos = []

while True:
    print("\n=== Novo orcamento ===")

    try:
        valor_pecas = float(input("Valor das pecas: R$ "))
        valor_mao_obra = float(input("Valor da mao de obra: R$ "))
        total = valor_pecas + valor_mao_obra

        prioridade = input("Prioridade (baixa/media/alta): ").strip().lower()

        if prioridade not in ["baixa", "media", "alta"]:
            print("Prioridade invalida.")
        else:
            if total >= 1000:
                classificacao = "Orcamento critico"
                soma_critica += 1
            elif total >= 500:
                classificacao = "Orcamento alto"
            else:
                classificacao = "Orcamento normal"

            if prioridade == "alta" and total >= 500:
                alerta = "Atencao: ordem prioritaria com orcamento alto"
            else:
                alerta = "Sem alerta especial"

            orcamento = {
                "valor_pecas": valor_pecas,
                "valor_mao_obra": valor_mao_obra,
                "total": total,
                "classificacao": classificacao,
                "prioridade": prioridade,
                "alerta": alerta
            }

            orcamentos.append(orcamento)

            ordem_valida += 1
            soma_total += total

            print("\n=== Resumo do orcamento ===")
            print(f"Valor das pecas: R$ {valor_pecas:.2f}")
            print(f"Valor da mao de obra: R$ {valor_mao_obra:.2f}")
            print(f"Total do orcamento: R$ {total:.2f}")
            print(f"Classificacao: {classificacao}")
            print(f"Prioridade: {prioridade}")
            print(f"Alerta: {alerta}")

    except ValueError:
        print("Erro: digite valores numericos validos.")

    continuar = input("Cadastrar outra ordem? (s/n): ").strip().lower()

    if continuar != "s":
        break

print("\n=== Resumo geral ===")
print(f"Ordens validas: {ordem_valida}")
print(f"Soma total dos orcamentos: R$ {soma_total:.2f}")
print(f"Orcamentos criticos: {soma_critica}")

print("\n=== Orcamentos cadastrados ===")

for orcamento in orcamentos:
    print(
        f"Total: R$ {orcamento['total']:.2f} | "
        f"Prioridade: {orcamento['prioridade']} | "
        f"Classificacao: {orcamento['classificacao']}"
    )
