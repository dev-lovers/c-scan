import re
from collections import OrderedDict

from .lexer_rules import token_patterns


def clean_code(code):
    def remove_comments(code):
        pattern = r"//[^\n]*"
        return re.sub(pattern, "", code)

    def remove_spaces(code):
        pattern = r"[ \t]+"
        return re.sub(pattern, " ", code).replace("\n", " ").strip()

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
                if token.lastgroup == "ID":
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
            return repr((self.kind, self.value, self.position))
        return repr((self.kind, self.value))


class TokenStream:
    def __init__(self) -> None:
        self.tokens = []

    def add_token(self, value, kind):
        token = Token(value, kind)
        self.tokens.append(token)


class SymbolTable:
    def __init__(self) -> None:
        self.symbols = OrderedDict()

    def add_token(self, token: Token):
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
        self.pattern = "|".join(
            [f"(?P<{key}>{pattern})" for key, pattern in token_patterns.items()]
        )

    def identify_tokens(self, source_code):
        return re.finditer(self.pattern, source_code, re.VERBOSE | re.MULTILINE)