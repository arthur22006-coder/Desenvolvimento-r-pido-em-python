try:
    f = open('Nomes.txt')
    s = f.readline()
    i = (s.strip())
    print(i)
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Erro na abertura do arquivo")
except ValueError:
    print("Formato invalido")
except Exception as e:
    print(f"Erro inesperado:{e}")
    raise
