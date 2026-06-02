import json


ARQUIVO_CADASTROS = "cadastros.json"


def salvar_cadastros(cadastros):
    with open(ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)


def carregar_cadastros():
    try:
        with open(ARQUIVO_CADASTROS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
