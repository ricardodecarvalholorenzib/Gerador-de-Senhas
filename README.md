# 🔐 Gerenciador de Senhas

Gerador de senhas aleatórias desenvolvido em **Python**.

O projeto gera senhas de 16 caracteres usando letras, números e caracteres especiais e permite copiar a senha para a área de transferência.

> 🟢 **Status:** Working

## ✨ Funcionalidades

- 🔑 Geração automática de senhas de 16 caracteres
- 🔤 Letras maiúsculas e minúsculas
- 🔢 Números
- 🔣 Caracteres especiais
- 📋 Cópia para a área de transferência
- 🔄 Geração de novas senhas sem reiniciar o programa
- ⌨️ Controle por teclado
- ➕ Adicionar Senhas
- 👁 Visualizar senhas
- 🔒 Criptografia das senhas com segurança usando Fernet
- 📂 Todas as senhas salvas em um arquivo .json com criptografia Fernet

## 📚 O que aprendi

- Organização de um projeto Python em módulos
- Importação de funções entre arquivos
- Manipulação de arquivos JSON
- Uso de caminhos absolutos com `os.path`
- Criação de dados persistentes
- Conceitos básicos de criptografia
- Separação de responsabilidades entre módulos

## 🛠️ Tecnologias

- Python 3
- `pyperclip` — cópia para a área de transferência
- `fernet` — criptografia de senhas
- `json`- salva as senhas no arquivo .json

> ⚠️ O programa utiliza `msvcrt`, portanto foi desenvolvido principalmente para **Windows**.

## ▶️ Como executar

### 1. Tenha o Python instalado

Instale o **Python 3** na sua máquina.

### 2. Clone o repositório

```bash
git clone https://github.com/ricardodecarvalholorenzib/Gerenciador-de-Senhas.git
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
```bash
pip install fernet
```
```
pip install pwinput
```

### 4. Execute

```bash
python main.py
```

No Windows, caso `python` não funcione, tente:

```bash
py main.py
```

## 📁 Estrutura

```text
Gerenciador-de-Senhas/
├── $secure$/
├── cmds/
├── essencials/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📚 Objetivo

Projeto criado para praticar lógica de programação, strings, geração de valores aleatórios, entrada de teclado e utilização de uma biblioteca externa, salvamento de senhas criptografadas em .json, criptografia e segurança de dados.
