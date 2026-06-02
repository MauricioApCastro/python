from armazenamento import carregar_cadastros, salvar_cadastros
from menu import mostrar_menu
import cadastros as cad


def main():
    cadastros = carregar_cadastros()
    while True:
        escolha = mostrar_menu()
        if escolha == '1':
            cadastros = cad.cadastrar(cadastros)
            salvar_cadastros(cadastros)
        elif escolha == '2':
            cad.listar(cadastros)
        elif escolha == '3':
            print(f"Total de cadastros: {cad.contar(cadastros)}")
        elif escolha == '4':
            cadastros = cad.editar(cadastros)
            salvar_cadastros(cadastros)
        elif escolha == '5':
            cadastros = cad.remover(cadastros)
            salvar_cadastros(cadastros)
        elif escolha in ('6', 's', 'S'):
            print('Saindo...')
            break
        else:
            print('Opção inválida — tente novamente.')


if __name__ == '__main__':
    main()
