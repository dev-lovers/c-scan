from io import StringIO

from flask import Flask, render_template, request

from src.analyzer.lexer import Lexer, clean_code

app = Flask(__name__, template_folder="web/templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "source_file" not in request.files:
        return "Nenhum arquivo enviado.", 400

    file = request.files["source_file"]

    if file.filename == "":
        return "Nenhum arquivo selecionado.", 400

    file_memory = StringIO(file.read().decode("utf-8"))
    source_code = file_memory.getvalue()
    file_memory.close()

    cleaned_code = clean_code(source_code)

    lexer = Lexer(cleaned_code)
    stream, symbol_table = lexer.tokenize()

    result = f"<h3>Tokens Identificados:</h3><ul>"
    for token in stream.tokens:
        result += f"<li>Token: {token.value}, Tipo: {token.kind}</li>"
    result += "</ul>"

    result += f"<h3>Tabela de Símbolos:</h3><ul>"
    for symbol in symbol_table.symbols:
        result += f"<li>Símbolo: {symbol}</li>"
    result += "</ul>"

    return result


if __name__ == "__main__":
    app.run(debug=True)