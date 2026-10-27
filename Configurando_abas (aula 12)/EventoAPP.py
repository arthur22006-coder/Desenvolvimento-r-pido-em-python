import tkinter as tk
from tkinter import ttk

class EventoAPP:
    def __init__(self, raiz):
        raiz.title("Evento de botão")
        self.label = ttk.Label(raiz, text="Ola, Tkinter!")
        self.label.pack(pady=10)
        botao = ttk.Button(raiz, text="Clique em mim", command= self.clicado)

        botao.pack(pady=10)

    def clicado(self):
        self.label.config(text="Botão clicado!")

if __name__ == "__main__":
    raiz = tk.Tk()
    EventoAPP(raiz)
    raiz.mainloop()