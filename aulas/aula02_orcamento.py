valor_pecas = float(input("Valor das pecas: R$ "))
valor_mao_obra = float(input("Valor da mao de obra: R$ "))
total = valor_pecas + valor_mao_obra

if total >= 1000:
    classificacao = "Orcamento critico"
elif total >= 500:
    classificacao = "Orcamento alto"
else:
    classificacao = "Orcamento normal"

print(f"Valor das pecas: R$ {valor_pecas:.2f}")
print(f"Valor da mao de obra: R$ {valor_mao_obra:.2f}")
print(f"Total do orcamento: R$ {total:.2f}")
print(f"Classificacao: {classificacao}")
