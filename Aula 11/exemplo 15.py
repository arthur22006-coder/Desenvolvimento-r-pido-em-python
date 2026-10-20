import tkinter as tk
class GridApp :
    def __init__(self, raiz):
        raiz.title("Exemplo de sticky")
        raiz.columnconfigure(0, minsize =250)
        raiz.rowconfigure((0,1), minsize = 100)
        a = tk.Label(raiz, text= "A", bg="red", fg="white")
        a.grid(row=0 , column=0, sticky= "ne")
        b = tk.Label(raiz, text="B", bg="blue" , fg="white")
        b.grid(row=1, column=1, sticky="sw")

if __name__ == "__main__":
    raiz = tk.Tk()
    GridApp(raiz)
    raiz.mainloop()