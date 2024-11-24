# Analisador Léxico

Este projeto consiste em uma aplicação web desenvolvida com Flask que permite aos usuários fazer upload de um arquivo e realizar a análise léxica do seu conteúdo.

## Funcionalidades

* **Upload de Arquivo:** Permite o upload de arquivos de texto através de um formulário web.
* **Análise Léxica:** Realiza a análise léxica do conteúdo do arquivo, identificando os tokens presentes.
* **Exibição dos Resultados:** Apresenta os tokens identificados em uma tabela, com informações como tipo e lexema.

## Tecnologias Utilizadas

* **Flask:** Framework web para Python.
* **Python:** Linguagem de programação.
* **HTML:** Linguagem de marcação para a interface web.
* **CSS:** Linguagem de estilo para a interface web.
* **JavaScript:** Linguagem de script para interação do usuário.

## Como Executar

1. **Clonar o Repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   ```

2. **Criar um Ambiente Virtual:**
   ```bash
   python3 -m venv .venv
   ```

3. **Ativar o Ambiente Virtual:**
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Executar a Aplicação:**
   ```bash
   python run.py
   ```

6. **Acessar a Aplicação:**
    Abra seu navegador web e acesse `http://127.0.0.1:5000/`.

## Estrutura do Projeto

    ├── src
    │   ├── app.py          # Arquivo principal da aplicação Flask
    │   ├── analyzer        # Módulo com a lógica da análise léxica
    │   │   └── lexer.py    # Implementação do analisador léxico
    │   └── web             # Módulo com templates e arquivos estáticos
    │       ├── templates   # Arquivos HTML para a interface web
    │       └── static      # Arquivos CSS e JavaScript
    ├── run.py              # Script para executar a aplicação
    ├── requirements.txt    # Lista de dependências
    └── README.md           # Este arquivo

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Autor

* Joshua Britto
* Taciano Da Hora