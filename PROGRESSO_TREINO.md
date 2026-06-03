# Progresso do Treino

## Estado atual

O projeto chegou a uma versao final funcional de um sistema de equipamentos em Python.

Repositorio:

```text
https://github.com/MauricioApCastro/python
```

Arquivos principais:

```text
main.py
menu.py
cadastros.py
armazenamento.py
```

## O que o sistema faz

- Cadastra equipamentos.
- Lista todos os equipamentos.
- Busca equipamentos por marca.
- Busca equipamentos por cliente.
- Mostra total de cadastros.
- Edita cadastro por ID.
- Remove cadastro por ID.
- Salva e carrega dados em `cadastros.json`.

## Conceitos praticados

- Variaveis.
- Listas.
- Dicionarios.
- Funcoes.
- Parametros.
- `return`.
- `if`, `elif`, `else`.
- `while`.
- `for`.
- `try/except`.
- `True` e `False`.
- CRUD.
- JSON.
- Organizacao em modulos.
- Git e GitHub.
- Testes manuais.

## Mapa mental das funcoes

```text
cadastrar_equipamento -> retorna dicionario
formatar_dados -> retorna texto
contar_* -> retorna numero
listar_* -> imprime dados
editar_cadastro -> retorna True/False
remover_cadastro -> retorna True/False
salvar_cadastros -> salva arquivo JSON
carregar_cadastros -> retorna lista de cadastros
mostrar_menu -> imprime menu
ler_campo_obrigatorio -> retorna texto digitado
```

## Organizacao atual

```text
main.py
-> coordena o fluxo principal, menu, opcoes e chamadas das funcoes.

menu.py
-> contem mostrar_menu().

cadastros.py
-> contem as funcoes de cadastro, listagem, busca, contagem, edicao e remocao.

armazenamento.py
-> contem salvar_cadastros(), carregar_cadastros() e ARQUIVO_CADASTROS.
```

## Testes manuais feitos

- Listar com lista vazia.
- Mostrar total com lista vazia.
- Cadastrar equipamento.
- Listar equipamento cadastrado.
- Fechar e abrir novamente para testar JSON.
- Buscar por marca existente e inexistente.
- Buscar por cliente existente e inexistente.
- Editar com ID invalido.
- Editar com ID valido.
- Remover ID inexistente.
- Remover ID valido.

Resultado:

```text
Testes principais passaram.
```

## Ponto de atencao

O projeto ainda possui alguns arquivos gerados ou mudancas antigas no `git status`, como `__pycache__`, `cadastros.json` e possiveis delecoes antigas. No ultimo commit final foram enviados somente os arquivos-fonte principais.

## Proximo passo recomendado

Antes de avancar, fazer uma revisao curta:

```text
1. O que cada arquivo faz?
2. Quais funcoes retornam valor?
3. Quais funcoes apenas imprimem ou salvam?
4. Quando o sistema salva no JSON?
5. Por que o ID e necessario?
```

Depois, avancar para:

```text
SQLite
```

Objetivo do proximo bloco:

```text
Substituir cadastros.json por banco de dados SQLite.
Aprender tabela, INSERT, SELECT, UPDATE, DELETE e WHERE.
```

## Mensagem para continuar com o Codex

Use esta mensagem em outro computador:

```text
Quero continuar meu treinamento de Python/backend. O projeto atual esta no repositorio MauricioApCastro/python. Ja concluimos um CRUD de equipamentos em Python, organizado em modulos, com persistencia em JSON. Leia o arquivo PROGRESSO_TREINO.md e continue a partir dali, revisando rapidamente os conceitos antes de avancar para SQLite.
```

## Atualizacao de 2026-06-02

### Revisao geral concluida

Foi feita uma revisao geral para fechar a fase Python + CRUD + JSON.

Pontos que o aluno explicou corretamente:

- CRUD significa Create, Read, Update e Delete.
- Dividir o projeto em arquivos melhora a organizacao, a manutencao e a modularizacao.
- Neste projeto, um dicionario representa um cadastro e a lista guarda varios dicionarios.
- `return` devolve um valor para o programa usar; `print()` apenas mostra algo na tela.
- `cadastros.json` guarda a lista de cadastros para os dados nao sumirem ao fechar o programa.
- O ID e melhor para editar/remover porque nome, marca e outros campos podem se repetir; o ID funciona como chave primaria.

Resumo de entendimento:

```text
CRUD = criar, ler, atualizar e deletar dados
modulos = arquivos separados por responsabilidade
dicionario = um cadastro com chave e valor
lista = varios cadastros
return = devolve valor para o programa usar
print = apenas mostra na tela
JSON = persistencia em arquivo
ID = identificador unico/chave primaria
```

### Inicio do SQLite

Foi iniciado o estudo de SQLite em arquivo separado de treinamento.

Conceitos praticados:

- `import sqlite3`
- `sqlite3.connect("equipamentos.db")`
- `cursor = conexao.cursor()`
- `CREATE TABLE IF NOT EXISTS`
- `INTEGER PRIMARY KEY AUTOINCREMENT`
- `TEXT NOT NULL`
- `INSERT INTO`
- `VALUES (?, ?, ?, ?, ?)`
- `conexao.commit()`
- `SELECT * FROM equipamentos`
- `cursor.fetchall()`
- formatacao da listagem com indices de tupla
- `WHERE` como filtro
- `lower(campo) = ?`

O aluno criou o banco `equipamentos.db`, criou a tabela `equipamentos`, inseriu registros e listou dados formatados.

Exemplo de saida obtida:

```text
ID: 1 | Cliente: Joao | Equipamento: Notebook Dell Inspiron | Defeito: Nao liga
ID: 2 | Cliente: Joao | Equipamento: Notebook Dell Inspiron | Defeito: Nao liga
ID: 3 | Cliente: Joao | Equipamento: Notebook Dell Inspiron | Defeito: Nao liga
ID: 4 | Cliente: Joao | Equipamento: Notebook Dell Inspiron | Defeito: Nao liga
ID: 5 | Cliente: Joao | Equipamento: Notebook Dell Inspiron | Defeito: Nao liga
ID: 6 | Cliente: mauricio | Equipamento: notebook vaio rt6 | Defeito: nao apresentou defeitos
```

### Funcoes SQLite criadas ou iniciadas

Foi criada a funcao:

```python
def listar_equipamentos(cursor):
    cursor.execute("SELECT * FROM equipamentos")
    equipamentos = cursor.fetchall()

    for equipamento in equipamentos:
        print(
            f"ID: {equipamento[0]} | "
            f"Cliente: {equipamento[1]} | "
            f"Equipamento: {equipamento[2]} {equipamento[3]} {equipamento[4]} | "
            f"Defeito: {equipamento[5]}"
        )
```

Tambem foi criada a funcao de cadastro com `input()`:

```python
def cadastrar_equipamento(cursor):
    cliente = input("Nome do cliente: ")
    tipo = input("Tipo do equipamento: ")
    marca = input("Marca do equipamento: ")
    modelo = input("Modelo do equipamento: ")
    defeito = input("Defeito do equipamento: ")

    cursor.execute("""
    INSERT INTO equipamentos (cliente, tipo, marca, modelo, defeito)
    VALUES (?, ?, ?, ?, ?)
    """, (cliente, tipo, marca, modelo, defeito))
```

Foi iniciada a funcao de busca por marca:

```python
def buscar_por_marca(cursor):
    marca_busca = input("Digite a marca para buscar: ").strip().lower()

    cursor.execute("""
    SELECT * FROM equipamentos
    WHERE lower(marca) = ?
    """, (marca_busca,))

    equipamentos = cursor.fetchall()

    if not equipamentos:
        print("Nenhum equipamento encontrado para essa marca.")
        return

    for equipamento in equipamentos:
        print(
            f"ID: {equipamento[0]} | "
            f"Cliente: {equipamento[1]} | "
            f"Equipamento: {equipamento[2]} {equipamento[3]} {equipamento[4]} | "
            f"Defeito: {equipamento[5]}"
        )
```

Teste feito:

- Buscar por marca existente retornou o cadastro do cliente Mauricio com marca Vaio.
- Buscar por marca inexistente retornou a mensagem de nenhum equipamento encontrado.

### Duvida trabalhada: tupla com um unico valor

O aluno travou no conceito:

```python
(marca_busca,)
```

Foi explicado:

```text
Tupla = grupo de valores.
("vaio") = string, nao tupla.
("vaio",) = tupla com um unico item.
```

Regra fixada:

```text
1 ?  -> (valor,)
2 ?  -> (valor1, valor2)
5 ?  -> (valor1, valor2, valor3, valor4, valor5)
```

Resumo importante:

```text
A quantidade de ? no SQL deve combinar com a quantidade de valores enviados.
Quando existe apenas um valor, usamos a virgula para o Python entender que e uma tupla de um item.
```

Exercicio mental feito:

```python
dados = ("Joao", "Notebook", "Dell")

print(dados[0])
print(dados[1])
print(dados[2])
```

O aluno respondeu corretamente que apareceria uma string por linha:

```text
Joao
Notebook
Dell
```

### Ponto exato para continuar

Continuar devagar a partir de SQLite, retomando:

```text
connect() abre o banco
cursor.execute() executa comandos SQL
WHERE filtra resultados
fetchall() pega todos os resultados
? recebe valores enviados por tupla
```

Proximo exercicio recomendado:

Criar e testar:

```python
def buscar_por_cliente(cursor):
    cliente_busca = input("Digite o cliente para buscar: ").strip().lower()

    cursor.execute("""
    SELECT * FROM equipamentos
    WHERE lower(cliente) = ?
    """, (cliente_busca,))

    equipamentos = cursor.fetchall()

    if not equipamentos:
        print("Nenhum equipamento encontrado para esse cliente.")
        return

    for equipamento in equipamentos:
        print(
            f"ID: {equipamento[0]} | "
            f"Cliente: {equipamento[1]} | "
            f"Equipamento: {equipamento[2]} {equipamento[3]} {equipamento[4]} | "
            f"Defeito: {equipamento[5]}"
        )
```

Depois disso:

```text
1. Reforcar SELECT com WHERE.
2. Criar busca por cliente.
3. Ensinar UPDATE para editar por ID.
4. Ensinar DELETE para remover por ID.
5. So depois migrar o projeto principal de JSON para SQLite.
```

### Estrategia de portfolio e empregabilidade

Foi conversado que o aluno ja tem projetos publicados no GitHub:

```text
https://github.com/MauricioApCastro
```

Repositorios observados:

```text
Ipi_Manager
Bga-Curver-Mapper
Visualizador-de-Placas
gmail_cleaner
```

O aluno informou que publicou o `gmail_cleaner` no LinkedIn e que o `Ipi_Manager` ja foi instalado na escola de informatica da esposa.

Isso muda a prioridade de portfolio, porque projeto usado em ambiente real tem mais peso.

Prioridade sugerida:

```text
1. Ipi_Manager
2. CRUD de equipamentos
3. Visualizador-de-Placas
4. gmail_cleaner
5. Bga-Curver-Mapper
```

Posicionamento recomendado:

```text
Desenvolvedor Python em transicao para full-stack,
com experiencia tecnica em eletronica, automacao e ferramentas internas.
```

Plano combinado:

```text
Trilha de estudo:
SQLite -> FastAPI -> PostgreSQL -> React

Trilha de portfolio:
Polir o Ipi_Manager como case real.
Melhorar README, prints, descricao do problema, como rodar e melhorias futuras.
Continuar usando LinkedIn para mostrar evolucao semanal.
```

Mensagem atualizada para continuar em outro computador:

```text
Quero continuar meu treinamento de Python/backend. O projeto esta no repositorio MauricioApCastro/python. Leia o PROGRESSO_TREINO.md. Ja fechamos CRUD modular com JSON, fizemos revisao geral, iniciamos SQLite com CREATE TABLE, INSERT, SELECT, WHERE e parametros com ?. Eu me perdi um pouco em tuplas, entao retome devagar a regra 1 ? -> (valor,) antes de continuar. O proximo exercicio e criar buscar_por_cliente(cursor), depois UPDATE e DELETE por ID.
```
