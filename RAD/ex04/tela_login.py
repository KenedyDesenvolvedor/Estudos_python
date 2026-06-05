import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"}
}

def abrir_tela_login():
    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack()
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuarios[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario, usuario)
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(login_win, text="Entrar", command=validar_login).pack()
    login_win.mainloop()


def iniciar_sistema(tipo_usuario, usuario):
    janela = tk.Tk()
    janela.title("Sistema de Notas")
    janela.geometry("820x600")

    colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

    treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")

    for coluna in colunas:
        treeMedias.heading(coluna, text=coluna)
        treeMedias.column(coluna, width=120)

    treeMedias.pack(padx=10, pady=10)

    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
    treeMedias.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    carregar_dados(treeMedias, usuario, tipo_usuario)

    if tipo_usuario == "professor":
        tk.Button(janela, text="Cadastrar Aluno",
                  command=lambda: cadastrar_alunos(treeMedias)).pack()

        tk.Button(janela, text="Excluir Aluno",
                  command=lambda: excluir_aluno(treeMedias)).pack()

    janela.mainloop()


def carregar_dados(tree, usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilhaAlunos.xlsx", engine="openpyxl")
        tree.delete(*tree.get_children())

        for _, row in df.iterrows():

            if tipo_usuario == "professor" or row["Aluno"] == usuario:
                tree.insert(
                    '',
                    'end',
                    values=(
                        row["Aluno"],
                        row["Nota1"],
                        row["Nota2"],
                        row["Média"],
                        row["Situação"]
                    )
                )

    except FileNotFoundError:
        print("Nenhum dado encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")


def cadastrar_alunos(tree):
    nome = simpledialog.askstring("Cadastro", "Nome do Aluno:")
    nota1 = simpledialog.askfloat("Cadastro", "Nota 1:")
    nota2 = simpledialog.askfloat("Cadastro", "Nota 2:")

    if nome is None or nota1 is None or nota2 is None:
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
        values=(nome, nota1, nota2, f"{media:.2f}", situacao)
    )

    salvar_dados(tree)


def excluir_aluno(tree):
    selected = tree.selection()

    if not selected:
        messagebox.showerror("Erro", "Nenhum aluno selecionado.")
        return

    tree.delete(selected)
    salvar_dados(tree)


def salvar_dados(tree):
    dados = []

    for item in tree.get_children():
        dados.append(tree.item(item)["values"])

    df = pd.DataFrame(dados, columns=("Aluno", "Nota1", "Nota2", "Média", "Situação"))

    df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")

    print("Dados salvos com sucesso.")


abrir_tela_login()