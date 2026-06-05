import tkinter as tk

def submit():
    nome = nome_entry.get()
    email = email_entry.get()

    print("Nome:", nome)
    print("Email:", email)

root = tk.Tk()
root.title("Formulario de Inscrição")

t1= tk.Text(root, height=2, width=30)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

t1.insert(tk.END, "NOME \n")
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)
t1.pack()

t2= tk.Text(root, height=2, width=30)
t2.insert(tk.END, "EMAIL")
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

t2.pack()
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()