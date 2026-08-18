arquivo = open('C:/Users/Aluno/Downloads/VScode aula/Aula 2/manipulaçao arquivo/nomes.txt','w')
arquivo.write("Raphael")
arquivo.writelines(["\nCaroline", "\nVanessa","\nCristina"])
arquivo.close()

caminho_arquivo ='C:/Users/Aluno/Downloads/VScode aula/Aula 2/manipulaçao arquivo/nomes.txt'
arquivo = open (caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i,linha in  enumerate(linhas, start=1):
    print(f'Linha{i}: {linha}')