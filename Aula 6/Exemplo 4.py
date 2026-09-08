import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
dados_binarios_nome = os.path.join(diretorio_atual, "dados_puros.bin")

frase = "Raphael"
dados_binarios = frase.encode('utf-8')

try:
    with open(dados_binarios_nome, "wb") as salva_binario:
        salva_binario.write(dados_binarios)
    print("Dados binários salvos com sucesso")
except Exception as e:
    print(f"Ocorreu um erro ao salvar os dados binários: {e}")
if os.path.exists(dados_binarios_nome):
    try:
        with open(dados_binarios_nome, "rb") as carrega_binario:
            dados_carregados_bytes = carrega_binario.read()

            # 1. Decodifica de volta para o texto
            dados_carregados_texto = dados_carregados_bytes.decode('utf-8')

            # 2. Converte os bytes para uma string de zeros e uns separados por espaço
            binario_real = " ".join(f"{byte:08b}" for  byte in dados_carregados_bytes)

        print("Dados carregados com sucesso:")
        print(f"{binario_real} -> {dados_carregados_texto}")

    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados binários {e}")