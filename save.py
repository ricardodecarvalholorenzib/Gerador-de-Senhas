# save.py

# - importações
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # - diretório base do projeto
ARQUIVO = os.path.join(BASE_DIR, "$secure$", "passwords.json") # - caminho do arquivo de senhas

# - carregar senhas do arquivo JSON
def carregar_senhas():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f: # - abrir o arquivo de senhas em modo leitura
        try:
            return json.load(f)

        except json.JSONDecodeError:
            return []
 
# - salvar senhas no arquivo JSON
def salvar_senhas(senhas):
    with open(ARQUIVO, "w", encoding="utf-8") as f: # - abrir o arquivo de senhas em modo escrita
        json.dump(senhas, f, indent=4, ensure_ascii=False)

# - criar uma nova senha e salvar no arquivo JSON
def criar_senha(senha):
    from cmds.cryptography import criptografar_texto, obter_chave_salva

    key = obter_chave_salva()

    senha_cripto = criptografar_texto(senha, key)

    senhas_load = carregar_senhas()

    senhas_load.append({
        "senha": senha_cripto.decode("utf-8")
    }) # - adicionar a nova senha ao seu arquivo .json

    salvar_senhas(senhas_load)

    return True