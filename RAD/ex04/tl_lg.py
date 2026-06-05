import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import os

# =========================
# USUÁRIOS
# =========================
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}

tipo_usuario = None
usuario_logado = None
tree = None

ARQUIVO = "planilhaAlunos.xlsx"


# =========================
# LOGIN
# =========================
def abrir_login():
    login = tk.Tk()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Usuário").pack()
    ent_user = tk.Entry(login)
    ent_user.pack()

    tk.Label(login, text="Senha").pack()
    ent_pass = tk.Entry(login, show="*")
    ent_pass.pack()

    def validar():
        global tipo_usuario, usuario_logado

        user = ent_user.get()
        senha = ent_pass.get()

        if user in usuarios and usuarios[user]["senha"] == senha:
            tipo_usuario = usuarios[user]["tipo"]
            usuario_logado = user

            login.destroy()
            abrir_sistema()
        else:
            messagebox.showerror("Erro", "Login inválido!")

    tk.Button(login, text="Entrar", command=validar).pack()

    login.mainloop()


# =========================
# SISTEMA PRINCIPAL
# =========================
def abrir_sistema():
    global tree

    janela = tk.Tk()
    janela.title("Sistema de Notas")
    janela.geometry("800x500")

    tk.Label(
        janela,
        text=f"Usuário: {usuario_logado} ({tipo_usuario})",
        font=("Arial", 12)
    ).pack(pady=5)

    colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

    tree = ttk.Treeview(janela, columns=colunas, show="headings")

    for c in colunas:
        tree.heading(c, text=c)
        tree.column(c, width=120)

    tree.pack(pady=10)

    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    carregar_dados()

    # BOTÕES (SÓ PROFESSOR)
    if tipo_usuario == "professor":
        tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
        tk.Button(janela, text="Excluir", command=excluir).pack(pady=5)

    janela.mainloop()


# =========================
# DADOS
# =========================
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return

    try:
        df = pd.read_excel(ARQUIVO, engine="openpyxl")

        tree.delete(*tree.get_children())

        for _, row in df.iterrows():
            if tipo_usuario == "professor" or row["Aluno"] == usuario_logado:
                tree.insert(
                    "",
                    "end",
                    values=(
                        row["Aluno"],
                        row["Nota1"],
                        row["Nota2"],
                        row["Média"],
                        row["Situação"],
                    ),
                )

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar: {e}")


def salvar_dados():
    dados = []

    for item in tree.get_children():
        dados.append(tree.item(item)["values"])

    df = pd.DataFrame(
        dados,
        columns=("Aluno", "Nota1", "Nota2", "Média", "Situação")
    )

    df.to_excel(ARQUIVO, index=False, engine="openpyxl")


# =========================
# AÇÕES
# =========================
def cadastrar():
    nome = simpledialog.askstring("Cadastro", "Nome do aluno:")
    nota1 = simpledialog.askfloat("Cadastro", "Nota 1:")
    nota2 = simpledialog.askfloat("Cadastro", "Nota 2:")

    if not nome or nota1 is None or nota2 is None:
        return

    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    tree.insert(
        "",
        "end",
        values=(nome, nota1, nota2, f"{media:.2f}", situacao),
    )

    salvar_dados()


def excluir():
    selecionado = tree.selection()

    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um aluno!")
        return

    tree.delete(selecionado)
    salvar_dados()


# =========================
# START
# =========================
abrir_login()