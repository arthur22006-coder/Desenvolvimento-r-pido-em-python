from tkinter import Tk
janela = Tk()
janela.title("Nos python")
#Opcional no Windows:janela.iconbitmap("icon.ico")
janela.geometry("600x250")
janela.eval('tk::PlaceWindow . center')
janela.mainloop()