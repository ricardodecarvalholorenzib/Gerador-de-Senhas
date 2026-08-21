import os
import msvcrt

# Sistema de navegação com setas
def menu_interativo(titulo, opcoes):
    selecionado = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{titulo}\n")

        for i, opcao in enumerate(opcoes):
            if i == selecionado:
                print(f" ➤  {opcao}")
            else:
                print(f"   {opcao}")

        tecla = msvcrt.getch()

        if tecla in (b'\x00', b'\xe0'):
            tecla = msvcrt.getch()

        if tecla == b'H':    # Seta para Cima
            selecionado = (selecionado - 1) % len(opcoes)
        elif tecla == b'P':  # Seta para Baixo
            selecionado = (selecionado + 1) % len(opcoes)
        elif tecla == b'\r':  # ENTER
            return selecionado