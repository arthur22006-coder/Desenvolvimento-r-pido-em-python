import tkinter as tk

class GridResponsivoApp:
    def __init__(self, raiz):
        for posicao in range (3):
            raiz.columnconfigure(posicao,weight=5, minsize=100)
            raiz.rowconfigure(posicao, weight = 5, minsize= 75)
        for linha in range(3):
            texto = f"{linha}, {coluna}"
            label = tk.Label(raiz, text = texto, relief=tk.RAISED)
            label.grid(row=linha, column=coluna, padx=10, pady=10, sticky= "nsew")
if __name__ == "__main__":
    raiz = tk.Tk()
    GridResponsivoApp(raiz)
    raiz.mainloop()