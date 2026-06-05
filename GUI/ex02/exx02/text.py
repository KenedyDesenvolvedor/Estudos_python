import tkinter as tk
janela = tk.Tk()
T = tk.Text(janela, height=3, width=30)
T.pack()
T.insert(tk.END, "Este é um texto \nCom duas linhas height= 2\nCom Tres linhas height= 3")
tk.mainloop()