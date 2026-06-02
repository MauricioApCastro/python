def _next_id(cadastros):
    if not cadastros:
        return 1
    return max(item.get('id', 0) for item in cadastros) + 1


def formatar_dado(texto):
    return texto.strip()


def cadastrar(cadastros):
    nome = input('Nome: ').strip()
    idade = input('Idade: ').strip()
    email = input('Email: ').strip()
    try:
        idade = int(idade)
    except ValueError:
        idade = None
    novo = {'id': _next_id(cadastros), 'nome': formatar_dado(nome), 'idade': idade, 'email': formatar_dado(email)}
    cadastros.append(novo)
    print('Cadastro criado:', novo)
    return cadastros


def listar(cadastros):
    if not cadastros:
        print('Nenhum cadastro encontrado.')
        return
    print('\n--- Lista de Cadastros ---')
    for c in cadastros:
        print(f"ID: {c.get('id')} | Nome: {c.get('nome')} | Idade: {c.get('idade')} | Email: {c.get('email')}")


def contar(cadastros):
    return len(cadastros)


def _encontrar_por_id(cadastros, id_busca):
    for i, c in enumerate(cadastros):
        if c.get('id') == id_busca:
            return i, c
    return None, None


def editar(cadastros):
    try:
        id_str = input('ID do cadastro a editar: ').strip()
        id_busca = int(id_str)
    except ValueError:
        print('ID inválido.')
        return cadastros
    idx, registro = _encontrar_por_id(cadastros, id_busca)
    if registro is None:
        print('Cadastro não encontrado.')
        return cadastros
    nome = input(f"Nome [{registro.get('nome')}]: ").strip() or registro.get('nome')
    idade = input(f"Idade [{registro.get('idade')}]: ").strip() or registro.get('idade')
    email = input(f"Email [{registro.get('email')}]: ").strip() or registro.get('email')
    try:
        idade = int(idade) if idade is not None else None
    except ValueError:
        idade = registro.get('idade')
    cadastros[idx] = {'id': id_busca, 'nome': formatar_dado(nome), 'idade': idade, 'email': formatar_dado(email)}
    print('Cadastro atualizado.')
    return cadastros


def remover(cadastros):
    try:
        id_str = input('ID do cadastro a remover: ').strip()
        id_busca = int(id_str)
    except ValueError:
        print('ID inválido.')
        return cadastros
    idx, registro = _encontrar_por_id(cadastros, id_busca)
    if registro is None:
        print('Cadastro não encontrado.')
        return cadastros
    confirm = input(f"Confirma remoção de '{registro.get('nome')}'? (s/N): ").strip().lower()
    if confirm == 's':
        cadastros.pop(idx)
        print('Cadastro removido.')
    else:
        print('Remoção cancelada.')
    return cadastros
