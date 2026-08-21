# pass_new.py

# imports
import pwinput
import time

from cmds.save import criar_senha

def create_pass():
    print("Digite sua senha.\n")

    senha = pwinput.pwinput(prompt="> ", mask="#")

    sucesso = criar_senha(senha)
    if not sucesso:
        print("Erro!")

    else:
        print("\nSenha salva com sucesso!")
        time.sleep(2)

        from essencials.start import inicio
        inicio()