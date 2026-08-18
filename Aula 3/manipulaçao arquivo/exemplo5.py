import os 

diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))

diretorio_base = 'C:\\Users\\Aluno\\Downloads\\VScode aula\\'
subdiretorio = 'Aula 03\\manipulaçao arquivo'
nome_arquivo = 'dados.txt'
caminho_relativo = os.path.join(diretorio_base,subdiretorio,nome_arquivo)
caminho_absoluto = os.path.abspath(caminho_relativo)
print(f'Caminho relativo: {caminho_relativo}')
print(f'Caminho absoluto: {caminho_absoluto}')

print(f''' Todos os caminhos feitos aqui são apenas junções de strings, apenas o {diretorio_arquivo} realmente é um caminho válido nesse diretorio. ''')