import time
from typing import Generator, Any
def get_coxinhas (*pedidos) -> list: # * == argumento variado
    print("--- [Return] Preparando TODA a fornada de coxinhas de uma vez...")
    time.sleep(1)# Simula um procosso demorado
    return[f'[pedido]coxinhas'for pedido in pedidos]

def get_joelho (*pedidos) -> Generator[Any,Any,Any]:
    for pedido in pedidos:
        print(f"[Yield] Saindo um pedido de {pedido} joelho(s) agora!")
        time.sleep(1) #simula o tempo de fritar um por um
        yield f'{pedido} joelhos(s)'

if __name__ == "__main__":
    print ("SOLICITANDO COXINHAS (Return):")
    salgados_return = get_coxinhas (4,6,8)
    print("Recebi a lista completa:", salgados_return)

    print("\n" + "="*30 + "\n")
    print("SOLICITANDO JOELHOS (Yield):")
    pedidos_joelho = get_joelho (4,6,8)
    for salgados in pedidos_joelho:
        print(f"Cliente recebeu {salgados}")