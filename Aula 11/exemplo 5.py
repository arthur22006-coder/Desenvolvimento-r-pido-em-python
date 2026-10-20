import tkinter as tk
from tkinter import messagebox

def mostrar_nome():
    nome = entrada.get().strip()
    if nome:
        messagebox.showinfo("Cadastro",f"olá, {nome}!")
    else:
        messagebox.showwarning ("Atenção", "Infome seu nome.")

janela = tk.Tk()
tk.Label(janela, text="Nome:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(padx = 16)
tk.Button(janela, text="Enviar", command=mostrar_nome).pack(pady=10)
janela.mainloop()