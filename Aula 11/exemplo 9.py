import tkinter as tk

class PackApp:
    def __init__(self, raiz):
        tamanhos = [(100, "red"), (50, "green"),
                    (25, "blue")]
        for tamanho, cor in tamanhos:
            frame = tk.Frame(
                raiz, width = tamanho, height = tamanho, bg = cor 
            )

            frame.pack()
if __name__ == "__main__":
    raiz = tk.Tk()
    PackApp(raiz)
    raiz.mainloop()