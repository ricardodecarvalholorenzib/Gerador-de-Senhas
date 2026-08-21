# view_pass.py

# imports
import time
import msvcrt

from cmds.save import carregar_senhas
from cmds.cryptography import descriptografar_texto, obter_chave_salva

def view_passwords():
    senhas = carregar_senhas()

    key = obter_chave_salva()

    if senhas:
        from essencials.start import inicio

        print("Senhas:")
        for senha in senhas:
            senha_criptografada = senha["senha"]
            senha_descrypto = descriptografar_texto(senha_criptografada, key)
            print(f"{senha_descrypto}\n\n")

        tecla = msvcrt.getch()

        if tecla == b'\r':
            inicio()

        else:
            return view_passwords()

    else:
        print("Você não tem senhas salvas!")
        time.sleep(1)
        from essencials.start import inicio
        inicio()