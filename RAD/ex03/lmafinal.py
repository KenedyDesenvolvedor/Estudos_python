import tkinter as tk
from tkinter import ttk
import pandas as pd

# =========================
# CONFIGURAÇÃO DA JANELA
# =========================
janela = tk.Tk()
janela.title("Sistema de Cadastro de Alunos")
janela.geometry("820x600")

# =========================
# LABELS
# =========================
lblNome = tk.Label(janela, text="Nome do Aluno:")
lblNota1 = tk.Label(janela, text="Nota 1:")
lblNota2 = tk.Label(janela, text="Nota 2:")

# =========================
# ENTRADAS
# =========================
txtNome = tk.Entry(janela, bd=3, width=40)
txtNota1 = tk.Entry(janela, width=20)
txtNota2 = tk.Entry(janela, width=20)

# =========================
# POSICIONAMENTO DOS CAMPOS
# =========================
lblNome.pack(pady=5)
txtNome.pack(pady=5)

lblNota1.pack(pady=5)
txtNota1.pack(pady=5)

lblNota2.pack(pady=5)
txtNota2.pack(pady=5)

# =========================
# TABELA
# =========================
colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

treeMedias = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings",
    height=15
)

for coluna in colunas:
    treeMedias.heading(coluna, text=coluna)
    treeMedias.column(coluna, width=140, anchor="center")

# Scrollbar
scrollbar = ttk.Scrollbar(
    janela,
    orient="vertical",
    command=treeMedias.yview
)

treeMedias.configure(yscrollcommand=scrollbar.set)

# =========================
# FUNÇÕES
# =========================
def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado"

    elif media >= 5:
        situacao = "Recuperação"

    else:
        situacao = "Reprovado"

    return media, situacao


def salvar_dados():
    try:
        dados = []

        for linha in treeMedias.get_children():
            valores = treeMedias.item(linha)["values"]
            dados.append(valores)

        df = pd.DataFrame(dados, columns=colunas)

        df.to_excel(
            "planilhaAlunos.xlsx",
            index=False,
            engine="openpyxl"
        )

        print("Dados salvos com sucesso.")

    except Exception as erro:
        print(f"Erro ao salvar dados: {erro}")


def cadastrar_aluno():
    try:
        nome = txtNome.get().strip()

        if nome == "":
            print("Digite o nome do aluno.")
            return

        nota1 = float(txtNota1.get())
        nota2 = float(txtNota2.get())

        if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
            print("As notas devem estar entre 0 e 10.")
            return

        media, situacao = verificar_situacao(nota1, nota2)

        treeMedias.insert(
            "",
            "end",
            values=(
                nome,
                nota1,
                nota2,
                f"{media:.2f}",
                situacao
            )
        )

        salvar_dados()

    except ValueError:
        print("Digite notas numéricas válidas.")

    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")


def carregar_dados_iniciais():
    try:
        df = pd.read_excel(
            "planilhaAlunos.xlsx",
            engine="openpyxl"
        )

        for _, row in df.iterrows():

            treeMedias.insert(
                "",
                "end",
                values=(
                    row["Aluno"],
                    row["Nota1"],
                    row["Nota2"],
                    row["Média"],
                    row["Situação"]
                )
            )

        print("Dados carregados com sucesso.")

    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Um novo será criado.")

    except Exception as erro:
        print(f"Erro ao carregar arquivo: {erro}")


# =========================
# BOTÃO
# =========================
btnCadastrar = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar_aluno,
    bg="green",
    fg="white",
    width=20
)

btnCadastrar.pack(pady=10)

# =========================
# EXIBIÇÃO DA TABELA
# =========================
treeMedias.pack(padx=10, pady=10)

scrollbar.pack(side="right", fill="y")

# =========================
# INICIAR DADOS
# =========================
carregar_dados_iniciais()

# =========================
# LOOP PRINCIPAL
# =========================
janela.mainloop()