import tkinter as tk
from tkinter import ttk
from appDB import appDB

class PrincipalDB:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gestão de Produtos")

        self.lblCodigo = tk.Label(root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1)
        self.txtCodigo.config(state="readonly")

        self.lblNome = tk.Label(root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblPreco = tk.Label(root, text="Preço")
        self.lblPreco.grid(row=2, column=0)
        self.txtPreco = tk.Entry(root)
        self.txtPreco.grid(row=2, column=1)

        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnCadastrar.grid(row=3, column=0)
        
        self.btnAtualizar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnAtualizar.grid(row=3, column=1)

        self.btnExcluir = tk.Button(root, text="Excluir", command=self.fExcluirProduto)
        self.btnExcluir.grid(row=3, column=2)

        self.btnLimpar = tk.Button(root, text="Limpar", command=self.fLimparTela)
        self.btnLimpar.grid(row=3, column=3)

        self.tree = ttk.Treeview(root, columns=("CODIGO", "NOME", "PRECO"), show='headings')

        self.tree.heading("CODIGO", text="Código")
        self.tree.heading("NOME", text="Nome")
        self.tree.heading("PRECO", text="Preço")
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind('<ButtonRelease-1>', self.apresentarRegistrosSelecionados)

        self.carregarDadosIniciais()

    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get().strip()
        nome = self.txtNome.get().strip()
        preco = self.txtPreco.get().strip()
        
        if not nome or not preco:
            print("Preencha todos os campos.")
            return
        
        try:
            preco = float(preco.replace(",", "."))

        except ValueError:
            print("Preço invalido.")
            return
        
        self.db.inserir_dados(nome, preco)

        #insert manual 
        #self.tree.insert("", "end", values=(codigo, nome, preco))
        
        self.carregarDadosIniciais()
        self.fLimparTela()

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get().strip()
        nome = self.txtNome.get().strip()
        preco = self.txtPreco.get().strip()

        if not codigo:
            print("Selecione um produto")
            return
        
        if not nome or not preco:
            print("Preencha todos os campos.")
            return
        
        try:
            preco = float(preco.replace(",", "."))

        except ValueError:
            print("Preço invalido.")
            return
        
        self.db.atualizar_dados(codigo, nome, preco)
        
        self.carregarDadosIniciais()
        self.fLimparTela()
    
    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        self.fLimparTela()
        self.carregarDadosIniciais()
    
    def fLimparTela(self):
        self.txtCodigo.config(state="normal")
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.config(state="readonly")

        self.txtNome.delete(0, tk.END)

        self.txtPreco.delete(0, tk.END)
    
    def apresentarRegistrosSelecionados(self, event):
        selecionado = self.tree.selection()

        if not selecionado:
            return
        
        item = selecionado[0]

        valores= self.tree.item(item, "values")

        self.txtCodigo.config(state="normal")
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])
        self.txtCodigo.config(state="readonly")

        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])

        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])

    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

root = tk.Tk()
app_db = appDB()
app_gui = PrincipalDB(root,app_db)
root.mainloop()