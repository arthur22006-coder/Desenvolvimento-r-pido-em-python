#Cria um arquivo de exemplo e escreve um conteúdo nele.
with open("exemplo.txt","w",encoding = "utf-8") as f:
    f.write("Exemplo de uso dos métodos seek() e tell() em Python")

# Abre o arquivo para leitura e demonstra o uso de seek() e tell()
with open("exemplo.txt", "r", encoding="utf=-8") as f:
    #posição inicial do cursor
    print("Posição inicial do cursor:",f.tell())

    conteudo = f.read(10)
    print("Conteudo lido:", conteudo)
    print("Posição do cursor  após ler 10 caracteres:", f.tell())

    f.seek(0, 0) #whence=0: início do arquivo
    print("Posição do cursor após seek(0, 0):",f.tell())

    #Avança 15 caracteres a partir do início do arquivo
    f.seek(15, 0)
    print("Posição do cursor após seek(15, 0):", f.tell())
    parte = f.read(5)
    print("Conteúdo lido após seel(15,0):",parte)

    #Retrocede 5 caracteres a partir da posição atual usando seek absoluto
    pos_atual =  f.tell()
    f.seek(pos_atual -5, 0 ) #Calcula a  nova posição de forma absoluta
    print("Posição do cursor após retroceder 5 caracteres:",f.tell())
    parte2 = f.read(5)
    print("Conteudo lido após retroceder 5 caracteres:", parte2)

    #Move para o fim do arquivo
    f.seek(0, 2) #whence=2: fim do arquivo
    print("Posição do cursor no fim do arquivo:", f.tell())