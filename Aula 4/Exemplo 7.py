import re
def verifica_regex(texto: str) -> None:
    padrao = r'\(\d{3}\)  \d{3}\-\d{4}'
    # Padrão para encontrar números de telefone no formato (XXX) XXX-XXXX
    resultado = re.search(padrao, texto)
    if resultado:
        numeero_telefone = resultado.group()
        print("Número de telefone encontrado:", numero_telefone)
    else:
        print("Número de telefone não encontrado:")


if __name__ == "__main__":
    verifica_regex("O número de telefone de Raphael é (123) 456-7890.")