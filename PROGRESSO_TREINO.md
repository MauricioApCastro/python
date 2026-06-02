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
