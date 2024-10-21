"""
    Análise Léxica

    - Este programa realiza a análise léxica de um arquivo de entrada, a primeira etapa da compilação. Ele lê o código fonte caractere a caractere, transformando-o em uma sequência de tokens, que representam elementos da linguagem, como palavras reservadas, identificadores, números, operadores e pontuação.
"""

# TODO: 1º ETAPA - Simples varredura removendo comentários e espaços em branco
# TODO: 2º ETAPA - Quebrar o texto em lexemas
# TODO: 3º ETAPA - Identificar os tokens
# TODO: 4º ETAPA - Criar a tabela de símbolos

import re
from pathlib import Path

FILENAME = 'test.txt'
DIRECTORY_PATH = Path('tests')
FILEPATH = DIRECTORY_PATH / FILENAME

def clean_code(code):
    def remove_comments(code):
        # Remove comentários de linha
        pattern = r'//[^\n]*'
        return re.sub(pattern, '', code)
    
    def remove_spaces(code):
        # Remove espaços em branco, mas preserva quebras de linha
        pattern = r'[ \t]+'
        return re.sub(pattern, ' ', code).replace('\n', ' ').strip()
    
    return remove_spaces(remove_comments(code))


class Token:
    def __init__(self, value, kind) -> None:
        self.value = value
        self.kind = kind
    

class TokenStream:
    def __init__(self) -> None:
        self.tokens = []
    
    def add_token(self, value, kind):
        self.tokens.append(Token(value, kind))


class SymbolTable:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    try:
        with open(FILEPATH, 'r') as archive:
            code = archive.read()
            code = clean_code(code)
            stream = TokenStream()
            print(f"Código limpo:\n{code}\n")

            pattern = r'''
                (?P<KEYWORD>\b(?:int|float|double|char|void|if|else|for|while|do|return|switch|case|default|break|continue|goto|sizeof|struct|typedef|const|static|extern|volatile|enum|union|signed|unsigned|long|short)\b) |  # Palavras-chave C
                (?P<ID>(?:[a-zA-Z_][a-zA-Z_0-9]*)) |                      # Identificadores
                (?P<NUMBER>\b0[xX][0-9a-fA-F]+|0[0-7]*|\d+(\.\d+)?([eE][+-]?\d+)?\b) |  # Números: hexadecimais, octais, inteiros, decimais, notação científica
                (?P<CHAR>'(\\.|[^\\'])') |                             # Caracteres (com escape ou sem)
                (?P<STRING>"(\\.|[^\\"])*") |                          # Strings (com escape ou sem)
                (?P<DELIMITER>;)|                                      # Delimitadores (ponto e vírgula)
                (?P<OPERATOR>(==|!=|<=|>=|->|\+=|-=|\*=|/=|%=|=|\+|-|\*|/|%|&&|\|\||!|&|\||\^|<<|>>|,|\(|\)|\[|\]|\{|\}))  # Operadores e pontuação
            '''
        
            tokens = re.finditer(pattern, code, re.VERBOSE | re.MULTILINE)
            for token in tokens:
                if token.lastgroup:
                    stream.add_token(token.group(), token.lastgroup)
                    print((token.lastgroup, token.group()))
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{FILENAME}' não foi encontrado.")
