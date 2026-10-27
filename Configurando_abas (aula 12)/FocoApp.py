import tkinter as tk

class FocoApp:
    def __init__(self, raiz):
        self.textp_padrao = "Digite seu nome aqui!"
        self.entrada = tk.Entry(raiz, fg="gray", width=30)
        self.entrada.insert(0,self.textp_padrao)
        self.entrada.pack(pady=20)
        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)

    def limpar(self, _):
        if self.entrada.get() == self.textp_padrao:
            self.entrada.config(fg="black")

    def restaurar(self, _):
        if not self.entrada.get():
            self.entrada.insert(0, self.textp_padrao)
            self.entrada.config(fg="gray")

if __name__ == "__main__":
    raiz = tk.Tk()
    FocoApp(raiz)
    raiz.mainloop()