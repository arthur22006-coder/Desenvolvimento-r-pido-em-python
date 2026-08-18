linhas=[
    "Esta é a primeira linha.\n",
    "Esta é a segunda linha.\n",
    "Esta é a terceira linha.\n",
]
with open ("exemplo_writelines.txt","w", encoding="utf-8") as arquivo:
    # Escreve todas as linhas de uma vez no arquivo
    arquivo.writelines(linhas)

with open("exemplo_writelines.txt","r",encoding="utf-8")as arquivo:
    conteudo = arquivo.read()
    print("Conteudo do arquivo:")
    print(conteudo)