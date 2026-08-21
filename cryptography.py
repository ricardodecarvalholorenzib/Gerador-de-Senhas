# cryptography.py

# imports
import os

from cryptography.fernet import Fernet

CHAVE_FILE = "chave.key"

def gerar_chave():
    chave = Fernet.generate_key() # - gera a chave
    with open(CHAVE_FILE, "wb") as f:
        f.write(chave)
    return chave

def obter_chave_salva():
    if not os.path.exists(CHAVE_FILE): # - se a chave não existir, retorna uma nova
        return gerar_chave()
    
    with open(CHAVE_FILE, "rb") as f:
        return f.read()

def criptografar_texto(texto, chave):
    f = Fernet(chave)

    if isinstance(texto, str):
        bytes_text = texto.encode() # - transforma a senha em bytes

    else:
        bytes_text = texto

    texto_oculto = f.encrypt(bytes_text) # - encripta a senha
    return texto_oculto

def descriptografar_texto(texto_criptografado, chave):
    f = Fernet(chave)

    if isinstance(texto_criptografado, bytes): # - se o valor vier como bytes, converte para string primeiro se necessário
        texto_criptografado = texto_criptografado.decode('utf-8')
    
    if not isinstance(texto_criptografado, str): # - se o valor vier de algum outro modo, converte para string de qualquer forma
        texto_criptografado = str(texto_criptografado)

    texto_revelado = f.decrypt(texto_criptografado.encode()).decode() # - desencripta a senha
    return texto_revelado