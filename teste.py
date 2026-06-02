def mostrar_cliente(cadastro):
    print(cadastro["cliente"])


cadastros = [
    {"cliente": "Ana"},
    {"cliente": "João"}
]

for cadastro in cadastros:
    mostrar_cliente(cadastro)