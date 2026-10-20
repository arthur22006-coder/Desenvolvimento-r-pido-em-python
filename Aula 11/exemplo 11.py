import tkinter as tk

class PackSideApp:
    def __init__(self, raiz):
        faixas = [(100, "red"), (50, "green"),
                    (25, "blue")]
        for largura , cor in faixas:
            frame = tk.Frame(raiz, width= largura, bg = cor)
            frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
if __name__ == "__main__":
    raiz = tk.Tk()
    PackSideApp(raiz)
    raiz.mainloop()