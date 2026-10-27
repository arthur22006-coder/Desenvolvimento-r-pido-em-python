import tkinter as tk
from tkinter import messagebox

class DesafioCanvas:
    def __init__(self,raiz):
        self.canvas = tk.Canvas(raiz, width=240, height=120)
        self.retangulo = self.canvas.create_rectangle(60, 20, 180, 100, fill= "blue")
        self.canvas.pack(pady=10)
        tk.Button(raiz,text="Mudar cor",command=self.mudar_cor).pack()
        tk.Button(raiz, text="Avisar", command=self.avisar).pack()

    def mudar_cor(self):
        self.canvas.itemconfig(self.retangulo, fill = 'purple')

    def avisar(self):
        messagebox.showinfo("Aviso", "Você foi avisado")

raiz = tk.Tk()
DesafioCanvas(raiz)
raiz.mainloop()