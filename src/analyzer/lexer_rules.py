token_patterns = {
    'KEYWORD': r'\b(?:int|float|double|char|void|if|else|for|while|do|return|switch|case|default|break|continue|goto|sizeof|struct|typedef|const|static|extern|volatile|enum|union|signed|unsigned|long|short)\b',
    'ID': r'(?:[a-zA-Z_][a-zA-Z_0-9]*)',
    'NUMBER': r'\b0[xX][0-9a-fA-F]+|0[0-7]*|\d+(\.\d+)?([eE][+-]?\d+)?\b',
    'CHAR': r"'(\\.|[^\\'])'",
    'STRING': r'"(\\.|[^\\"])*"',
    'DELIMITER': r';',
    'OPERATOR': r'(==|!=|<=|>=|->|\+=|-=|\*=|/=|%=|=|\+|-|\*|/|%|&&|\|\||!|&|\||\^|<<|>>|,|\(|\)|\[|\]|\{|\})'
}
