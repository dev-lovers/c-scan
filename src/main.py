"""
    Análise Léxica

    - Este programa realiza a análise léxica de um arquivo de entrada, a primeira etapa da compilação. Ele lê o código fonte caractere a caractere, transformando-o em uma sequência de tokens, que representam elementos da linguagem, como palavras reservadas, identificadores, números, operadores e pontuação.
"""

# TODO: 1º ETAPA - Simples varredura removendo comentários e espaços em branco ✔️
# TODO: 2º ETAPA - Quebrar o texto em lexemas ✔️
# TODO: 3º ETAPA - Identificar os tokens ✔️
# TODO: 4º ETAPA - Criar a tabela de símbolos ✔️

import re
from pathlib import Path
from collections import OrderedDict

FILENAME = 'test.txt'
DIRECTORY_PATH = Path('tests')
FILEPATH = DIRECTORY_PATH / FILENAME

def clean_code(code):
    def remove_comments(code):
        pattern = r'//[^\n]*'
        return re.sub(pattern, '', code)
    
    def remove_spaces(code):
        pattern = r'[ \t]+'
        return re.sub(pattern, ' ', code).replace('\n', ' ').strip()
    
    return remove_spaces(remove_comments(code))


class Lexer:
    def __init__(self, source_code) -> None:
        self.source_code = source_code
        self.token_list = TokenStream()
        self.symbol_table = SymbolTable()

    def tokenize(self):
        token_identifier = TokenIdentifier()
        tokens = token_identifier.identify_tokens(self.source_code)

        for token in tokens:
            if token.lastgroup:
                token_obj = Token(token.group(), token.lastgroup)
                if token.lastgroup == 'ID':
                    position_symbol = self.symbol_table.add_token(token_obj)
                    self.token_list.add_token(position_symbol, token.lastgroup)
                else:
                    self.token_list.add_token(token_obj.value, token.lastgroup)

        return self.token_list, self.symbol_table
    

class Token:
    def __init__(self, value, kind=None, position=None) -> None:
        self.value = value
        self.kind = kind
        self.position = position

    def __repr__(self):
        if self.position is not None:
            return repr((self.value, self.kind, self.position))
        return repr((self.value, self.kind))


class TokenStream:
    def __init__(self) -> None:
        self.tokens = []
    
    def add_token(self, value, kind):
        token = Token(value, kind)
        self.tokens.append(token)


class SymbolTable:
    def __init__(self) -> None:
        self.symbols = OrderedDict()
    
    def add_token(self, token:Token):
        is_token_exist = self.check_if_token_exists(token)
        if is_token_exist:
            position = len(self.symbols) + 1
            self.symbols[token.value] = token.kind
            return position
        else:
            return self.get_token_position(token.value)

    def get_token_position(self, value):
        if value in self.symbols:
            return list(self.symbols.keys()).index(value) + 1
        return None
    
    def check_if_token_exists(self, token):
        return token.value not in self.symbols


class TokenIdentifier:
    def __init__(self) -> None:
        self.pattern = r'''
            (?P<KEYWORD>\b(?:int|float|double|char|void|if|else|for|while|do|return|switch|case|default|break|continue|goto|sizeof|struct|typedef|const|static|extern|volatile|enum|union|signed|unsigned|long|short)\b) |  
            (?P<ID>(?:[a-zA-Z_][a-zA-Z_0-9]*)) |                      
            (?P<NUMBER>\b0[xX][0-9a-fA-F]+|0[0-7]*|\d+(\.\d+)?([eE][+-]?\d+)?\b) |  
            (?P<CHAR>'(\\.|[^\\'])') |                             
            (?P<STRING>"(\\.|[^\\"])*") |                          
            (?P<DELIMITER>;)|                                     
            (?P<OPERATOR>(==|!=|<=|>=|->|\+=|-=|\*=|/=|%=|=|\+|-|\*|/|%|&&|\|\||!|&|\||\^|<<|>>|,|\(|\)|\[|\]|\{|\}))  
        '''

    def identify_tokens(self, source_code):
        return re.finditer(self.pattern, source_code, re.VERBOSE | re.MULTILINE)


if __name__ == "__main__":
    try:
        with open(FILEPATH, 'r') as archive:
            source_code = archive.read()
            source_code = clean_code(source_code)

            lexer = Lexer(source_code)
            stream, symbol_table = lexer.tokenize()

    except FileNotFoundError:
        print(f'Erro: O arquivo "{FILENAME}" não foi encontrado.')
    except IOError as e:
        print(f'Erro ao ler o arquivo: {e}')

