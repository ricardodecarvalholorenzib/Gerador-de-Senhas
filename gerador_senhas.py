# GERADOR SENHAS - VERSÃO: BETA

# ================================
# IMPORTS
import msvcrt
import pyperclip
import random
import string
# ================================

# ================================
# PROGRAMA PRINCIPAL
print("Pressione ENTER para gerar uma senha aleatória de 16 caracteres ou ESC para sair: ")

tecla = msvcrt.getch()

while True: # - Gera senha aleatória de 16 caracteres e pergunta se deseja copiar para a área de transferência
    if tecla == b'\r':
        caracteres = string.ascii_letters + string.digits + string.punctuation

        tamanho = 16

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        print(f"\nSua senha: {senha}\n")

        print("Copiar Senha para a área de transferência? (S/N)")

        tecla = msvcrt.getch()

        if tecla == b's' or tecla == b'S':
            pyperclip.copy(senha)
            print("\nSenha copiada para a área de transferência!")

            print("\nPressione ENTER para gerar outra senha ou ESC para sair: ") # - Repetir novamente o processo de gerar senha
            tecla = msvcrt.getch()
            if tecla == b'\r':
                print("Gerando nova senha...")
            else:
                break

        else:
            print("\nSenha não copiada.")

            print("\nPressione ENTER para gerar outra senha ou ESC para sair: ") # - Repetir novamente o processo de gerar senha
            tecla = msvcrt.getch()
            if tecla == b'\r':
                print("Gerando nova senha...")
            else:
                break
# ================================