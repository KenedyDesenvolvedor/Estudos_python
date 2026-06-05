from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# conexão com seu banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="kenedy",
        password="Kenydev123",
        database="meu_banco"
    )

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family: Arial; background:#111; color:white; text-align:center; }
        .box { margin-top:100px; }
        input { padding:10px; margin:5px; }
        button { padding:10px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Login</h1>
        <form method="POST">
            <input name="nome" placeholder="Usuário"><br>
            <input name="senha" type="text" placeholder="Senha"><br>
            <button type="submit">Entrar</button>
        </form>
        <p>{{msg}}</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def login():
    msg = ""
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE nome=%s AND senha=%s", (nome, senha))
        user = cursor.fetchone()

        if user:
            msg = "✅ Login realizado!"
        else:
            msg = "❌ Usuário ou senha inválidos"

        conn.close()

    return render_template_string(HTML, msg=msg)

app.run(debug=True)