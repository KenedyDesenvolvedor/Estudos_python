import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Aplicação GUI com o widget Label")
ttk.Label(janela, text="Componente label").grid(column=0, row=0)

janela.mainloop()