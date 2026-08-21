# start.py

from cmds.keys import menu_interativo # - importa o sistema de setas
from cmds.clean import limpar_tela

def inicio():
    menu = menu_interativo("Selecione uma opção abaixo:", ["1 - Nova Senha", "2 - Listar Senhas", "3 - Criar Senha Aleatória", "4 - Sair"]) # - menu que interage com as outras telas

    if menu == 0: # - se o usuário selecionar "1 - Nova Senha"
        from windows.pass_new import create_pass # - abre a tela de criar senha
        limpar_tela()
        create_pass()

    elif menu == 1: # - se o usuário selecionar "2 - Listar Senhas"
        from windows.view_pass import view_passwords # - abre a tela de visualizar as senhas
        limpar_tela()
        view_passwords()

    elif menu == 2: # - se o usuário selecionar "3 - Criar Senha Aleatória"
        from windows.random_pass import random_senha # - abre a tela de visualizar as senhas
        limpar_tela()
        random_senha()
        
inicio()