class Aluno:
    def __init__(self, nome:str, idade:int, nota:float) :
        self.nome = nome
        self.idade = idade
        self.nota = nota
        def calcular_media(self):
            return sum(self.notas) / len(self.notas)
if __name__ == "__main__":
    aluno1 = Aluno  ("Bernardo", 19,[8.0,7.0])
    aluno2 = Aluno  ("Arthur",19,[7.0,9.0])
    lista_alunos = [aluno1,aluno2]
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome} Média: {aluno.calcular_media():.2f}")
