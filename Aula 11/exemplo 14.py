import tkinter as tk
class GridResponsivoApp:
    def __init__(self, raiz):
        for posicao in range(3):
            raiz.columnconfigure(posicao, weight= 1, minsize = 75)
            raiz.rowconfigure(posicao, weight= 1, minsize = 50)
        for linha in range(3):
            for coluna in range(3):
                texto = f"(linha) ,(coluna)"
                label = tk.Label(raiz, text=texto, relief= tk.RAISED)
                label.grid(row = linha , column = coluna,
                       padx=5, pady= 5, sticky= "nsew")

if __name__ == "__main__":
    raiz = tk.Tk()
    GridResponsivoApp(raiz)
    raiz.mainloop()