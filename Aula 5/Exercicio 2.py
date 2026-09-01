def criar_registro_notas(arquivo):
    with open(arquivo,"w") as file:
        file.write("Registro de notas dos alunos\n")
        file.write("======================\n")

def adicionar_nota(arquivo,aluno,nota):
    with open(arquivo, "a") as file:
        file.write(f"Alunos:{aluno}\n")
        file.write(f"Notas:{nota}\n")
        file.write("======================\n")

if __name__ == "__main__" :
    registro_notas = "registro_notas.txt"
    criar_registro_notas(registro_notas)
    adicionar_nota(registro_notas, "Rapha",8.5)
    adicionar_nota(registro_notas, "Caroline",9.8)