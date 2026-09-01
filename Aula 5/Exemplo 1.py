def divide(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("Dividir por zero não é possível")
    else:
        print("Sua resposta é:", resultado)
    finally:
        print("Isso sempre acontecerá")


divide(3, 2)
divide(3, 0)