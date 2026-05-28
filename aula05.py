
valor_pecas = float(input("Valor das peças: R$: "))
valor_mao_obra = float(input("valor mão de obra: R$"))
total = valor_pecas + valor_mao_obra

if total >= 500:
    status = "Orçamento alto"
else:
    status = "Orçamento normal"


print(f"Valor das peças: R$ {valor_pecas:.2f}")
print(f"Valor do mao_obra: R$ {valor_mao_obra:.2f}")
print(f"Total do orçamento: R$ {total:.2f}")
print(f"Classificação: {status}")



