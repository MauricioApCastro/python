# Diario de Aulas

## Aula 01 - Entrada, saida e variaveis

- Usei `input()` para receber dados do usuario.
- Usei `print()` para mostrar dados na tela.
- Guardei informacoes em variaveis.
- Usei `f-string` para formatar textos.

Exemplo:

```python
nome_cliente = input("Nome do cliente: ")
print(f"Cliente: {nome_cliente}")
```

## Aula 02 - Numeros e calculos

- Aprendi que `input()` sempre retorna texto.
- Usei `float()` para converter texto em numero decimal.
- Calculei total de orcamento com soma.
- Usei `:.2f` para mostrar valores com duas casas decimais.

Exemplo:

```python
valor_pecas = float(input("Valor das pecas: R$ "))
valor_mao_obra = float(input("Valor da mao de obra: R$ "))
total = valor_pecas + valor_mao_obra

print(f"Total: R$ {total:.2f}")
```

## Aula 03 - Condicionais

- Usei `if`, `elif` e `else`.
- Classifiquei orcamentos como normal, alto ou critico.
- Aprendi que a ordem das condicoes importa.

Exemplo:

```python
if total >= 1000:
    classificacao = "Orcamento critico"
elif total >= 500:
    classificacao = "Orcamento alto"
else:
    classificacao = "Orcamento normal"
```

## Aula 04 - Validacao e normalizacao

- Usei `.strip()` para remover espacos no inicio e no fim.
- Usei `.lower()` para transformar texto em minusculo.
- Usei `not in` para verificar se um valor nao esta em uma lista de opcoes permitidas.
- Normalizei `media` para `media` acentuado no programa exibido ao usuario.

Exemplo:

```python
prioridade = input("Prioridade (baixa/media/alta): ").strip().lower()

if prioridade not in ["baixa", "media", "alta"]:
    print("Prioridade invalida.")
```

## Aula 05 - Tratamento de erros

- Usei `try/except` para evitar que o programa quebre quando o usuario digita texto no lugar de numero.
- Tratei `ValueError`.

Exemplo:

```python
try:
    valor = float(input("Valor: "))
except ValueError:
    print("Erro: digite um valor numerico valido.")
```

## Aula 06 - Lacos, contadores e acumuladores

- Usei `while True` para repetir cadastros.
- Usei `break` para encerrar o laco.
- Criei contadores para ordens validas.
- Criei acumuladores para somar valores.

Exemplo:

```python
ordem_valida = 0
soma_total = 0

while True:
    ordem_valida += 1
    soma_total += 100

    continuar = input("Continuar? (s/n): ").strip().lower()
    if continuar != "s":
        break
```

## Aula 07 - Listas e dicionarios

- Criei listas com `[]`.
- Criei dicionarios com pares `"chave": valor`.
- Usei `.append()` para adicionar um dicionario dentro de uma lista.
- Usei `for` para percorrer a lista.

Resumo mental:

```text
equipamento = um item
equipamentos = lista com varios itens
```

Exemplo:

```python
equipamentos = []

dados_equipamento = {
    "cliente": "Joao",
    "tipo": "Notebook",
    "defeito": "Nao liga"
}

equipamentos.append(dados_equipamento)
```

## Aula 08 - Funcoes e return

- Entendi que `return` devolve um valor para fora da funcao.
- O nome da variavel dentro da funcao pode ser diferente do nome fora.
- Usei nomes mais claros para reduzir confusao: `dados_equipamento`, `novo_equipamento`, `equipamentos`.

Fluxo:

```text
dados_equipamento
        -> return
novo_equipamento
        -> append
equipamentos
```

Exemplo:

```python
def cadastrar_equipamento():
    dados_equipamento = {
        "cliente": "Joao",
        "tipo": "Notebook"
    }

    return dados_equipamento


equipamentos = []
novo_equipamento = cadastrar_equipamento()
equipamentos.append(novo_equipamento)
```

## Aula 09 - Fixacao de funcoes, listas e dicionarios

Decisao tomada: antes de avancar para conteudos novos, vamos fixar bastante o que ja foi estudado.

Conceitos em revisao:

- dicionario guarda dados em pares de chave e valor;
- lista guarda varios itens em sequencia;
- `.append()` adiciona um item ao final de uma lista;
- `return` devolve um valor para quem chamou a funcao;
- `cadastro` representa um dicionario;
- `cadastros` representa uma lista com varios dicionarios;
- `for cadastro in cadastros` percorre cada dicionario da lista.

Respostas importantes consolidadas:

```text
cadastro = um registro individual
cadastros = lista com varios registros
```

```python
novo_cadastro = cadastrar_equipamento()
```

Significa:

```text
chama a funcao, recebe o valor retornado e guarda em novo_cadastro
```

```python
cadastros.append(novo_cadastro)
```

Significa:

```text
adiciona novo_cadastro dentro da lista cadastros
```

```python
for cadastro in cadastros:
    texto = formatar_dados(cadastro)
    print(texto)
```

Significa:

```text
para cada dicionario da lista, formata os dados e imprime o texto
```

## Metodo de fixacao

O treino agora deve propor uma necessidade pequena por vez e esperar o aluno resolver.

Exemplos de necessidades:

- mostrar o total de cadastros;
- contar cadastros por marca;
- buscar cadastros por cliente;
- filtrar cadastros por tipo;
- listar somente equipamentos de uma marca;
- revisar o que cada linha faz antes de criar novas funcoes.

Evitar avancar para assunto novo enquanto houver inseguranca em:

- funcao;
- parametro;
- `return`;
- lista;
- dicionario;
- `append`;
- `for`.

## Aula 10 - Inicio do menu do sistema

Necessidade trabalhada:

```text
Em vez de o programa executar tudo em sequencia, o usuario deve escolher o que quer fazer.
```

Menu planejado:

```text
=== Sistema de Equipamentos ===
1 - Cadastrar equipamento
2 - Listar todos
3 - Buscar por marca
4 - Buscar por cliente
5 - Mostrar total de cadastros
0 - Sair
```

Conceitos reforcados:

- uma funcao pode apenas imprimir, sem `return`;
- `mostrar_menu()` apenas exibe as opcoes;
- o `input("Escolha uma opcao")` precisa ficar dentro do `while`, porque o menu deve repetir;
- quando uma funcao retorna valor e esse retorno nao e guardado, ele se perde;
- funcoes que imprimem podem ser apenas chamadas;
- funcoes que retornam numero precisam ter o retorno guardado em variavel para depois imprimir.

Trecho atual do `while`:

```python
while True:
    mostrar_menu()
    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        novo_cadastro = cadastrar_equipamento()
        cadastros.append(novo_cadastro)
        print("Cadastro realizado com sucesso.")

    elif opcao == "2":
        listar_equipamentos(cadastros)

    elif opcao == "5":
        total_cadastros = contar_cadastros(cadastros)
        print(f"Total de equipamentos cadastrados: {total_cadastros}")

    elif opcao == "0":
        break

    else:
        print("Opcao invalida.")
```

Ponto de parada:

```text
Proxima aula: implementar a opcao 3 - Buscar por marca.
```

Antes de implementar, revisar:

```text
contar_por_marca -> retorna numero
listar_por_marca -> imprime dados
```
