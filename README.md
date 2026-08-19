# 🔐 Gerador de Senhas

Gerador de senhas aleatórias desenvolvido em **Python**.

O projeto gera senhas de 16 caracteres usando letras, números e caracteres especiais e permite copiar a senha para a área de transferência.

> 🟡 **Status:** Beta

## ✨ Funcionalidades

- 🔑 Geração automática de senhas de 16 caracteres
- 🔤 Letras maiúsculas e minúsculas
- 🔢 Números
- 🔣 Caracteres especiais
- 📋 Cópia para a área de transferência
- 🔄 Geração de novas senhas sem reiniciar o programa
- ⌨️ Controle por teclado

## 🛠️ Tecnologias

- Python 3
- `pyperclip` — cópia para a área de transferência
- `msvcrt` — leitura do teclado no Windows
- `random` e `string` — bibliotecas padrão do Python

> ⚠️ O programa utiliza `msvcrt`, portanto foi desenvolvido principalmente para **Windows**.

## ▶️ Como executar

### 1. Tenha o Python instalado

Instale o **Python 3** na sua máquina.

### 2. Clone o repositório

```bash
git clone https://github.com/ricardodecarvalholorenzib/Gerador-de-Senhas.git
cd Gerador-de-Senhas
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou, se preferir:

```bash
pip install pyperclip
```

### 4. Execute

```bash
python main.py
```

No Windows, caso `python` não funcione, tente:

```bash
py main.py
```

## 🎮 Como usar

- `ENTER` — gera uma senha
- `S` — copia a senha para a área de transferência
- `ENTER` — gera outra senha
- `ESC` — encerra o programa

## 📁 Estrutura

```text
Gerador-de-Senhas/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📚 Objetivo

Projeto criado para praticar lógica de programação, strings, geração de valores aleatórios, entrada de teclado e utilização de uma biblioteca externa.
