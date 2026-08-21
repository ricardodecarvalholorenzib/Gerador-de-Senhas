# random_pass.py

# importações
import msvcrt
import pyperclip
import random
import string
import time

from cmds.save import criar_senha

def random_senha():

    print("Pressione ENTER para gerar uma senha aleatória de 16 caracteres ou ESC para voltar ao menu: ")

    tecla = msvcrt.getch()

    if tecla == b'\r':
        caracteres = string.ascii_letters + string.digits + string.punctuation

        tamanho = 16

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # - Gera senha aleatória de 16 caracteres e pergunta se deseja copiar para a área de transferência

        print(f"\nSua senha: {senha}\n")

        print("Copiar Senha para a área de transferência? (S/N)")

        tecla = msvcrt.getch()

        if tecla == b's' or tecla == b'S':
            pyperclip.copy(senha)
            print("\nSenha copiada para a área de transferência!")

        print("Deseja salvar essa senha? (S/N)")

        tecla_salvar = msvcrt.getch()

        if tecla_salvar == b's' or tecla == b'S':
            sucesso = criar_senha(senha)
            if not sucesso:
                print("Erro!")

            else:
                print("\nSenha salva com sucesso!")
                time.sleep(2)

    elif tecla == b'\x1b':
        from essencials.start import inicio
        print("Voltando ao menu...")
        time.sleep(1.5)
        inicio()

    else:
        print("Erro!\n")
        return random_senha()
