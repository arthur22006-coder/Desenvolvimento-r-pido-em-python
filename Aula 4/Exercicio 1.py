import re
PADRAO_EMAIL = re.compile(r'^\w+([\.-]?\w+)*@\w{4.}+([\.-]?\w+)*(\-\w{2,3})+$')

def validar_email(email:list[str]) -> list[bool]:
    return bool (PADRAO_EMAIL.match(email))

if __name__ == "__main__":
    exemplo_emails = [
    "usuario@email.com", #valido
    "nome+tag@email.com",  #invalido
    "a@b.co", #invalido,dominio curto
    "usuario@email.co.uk", #valido
    "@email.com", #invalido sem usurario
    "usuario@.com", #invalido
    "usario@email", #invalido, sem TLD
    "usu ario@email.com", #invalido, espaço
    ]
    for email in exemplo_emails:
        if validar_email(email):
            print(f"{email}é um endereço de e-mail válido.")
        else:
            print(f"{email}não é um endereço de e-mail válido")