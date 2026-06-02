import json
import os

ARQUIVO_CADASTROS = 'cadastros.json'


def salvar_cadastros(cadastros):
    with open(ARQUIVO_CADASTROS, 'w', encoding='utf-8') as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=2)


def carregar_cadastros():
    if not os.path.exists(ARQUIVO_CADASTROS):
        return []
    with open(ARQUIVO_CADASTROS, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
