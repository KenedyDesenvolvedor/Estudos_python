import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("app")

# Adiciona um rótulo (Label)
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack() # Posiciona o widget na janela

tk.Button(janela, text="Close")

# Inicia a aplicação
janela.mainloop()
