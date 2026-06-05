from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

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
    <title>Sistema</title>
    <style>
        body {
            font-family: Arial;
            background: #111;
            color: white;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }
        .box {
            background:#222;
            padding:30px;
            border-radius:10px;
            width:300px;
        }
        input, button {
            width:100%;
            padding:10px;
            margin:5px 0;
        }
        button {
            background:#00ff88;
            border:none;
            cursor:pointer;
        }
        .msg { margin-top:10px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Login</h2>
        <form method="POST" action="/login">
            <input name="nome" placeholder="Usuário" required>
            <input name="senha" type="password" placeholder="Senha" required>
            <button>Entrar</button>
        </form>

        <h2>Cadastro</h2>
        <form method="POST" action="/cadastro">
            <input name="nome" placeholder="Novo usuário" required>
            <input name="senha" type="password" placeholder="Senha" required>
            <button>Cadastrar</button>
        </form>

        <p class="msg">{{msg}}</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, msg="")

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    nome = request.form["nome"]
    senha = request.form["senha"]

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nome=%s AND senha=%s", (nome, senha))
    user = cursor.fetchone()

    conn.close()

    if user:
        return render_template_string(HTML, msg="✅ Login realizado!")
    else:
        return render_template_string(HTML, msg="❌ Usuário ou senha inválidos")

# CADASTRO
@app.route("/cadastro", methods=["POST"])
def cadastro():
    nome = request.form["nome"]
    senha = request.form["senha"]

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (nome, senha))
        conn.commit()
        msg = "✅ Usuário cadastrado!"
    except:
        msg = "❌ Erro (usuário pode já existir)"

    conn.close()

    return render_template_string(HTML, msg=msg)

app.run(debug=True)