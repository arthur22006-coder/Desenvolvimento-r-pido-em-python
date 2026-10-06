from pathlib import Path


class Pedido:

    def __init__(
        self: object,
        codigo: int,
        cliente: str,
        produto: str,
        email: str,
        quantidade: int,
        preco_unit: float,
    ):
        self.codigo = codigo
        self.cliente = cliente
        self.produto = produto
        self.email = email
        self.quantidade = quantidade
        self.preco_unit = preco_unit

    def converter_txt(self):
        return f"{self.codigo};{self.cliente};{self.email};{self.produto},{self.quantidade},{self.preco_unit}"

    def calc_total(self):
        total = self.quantidade * self.preco_unit
        return total


class ImportadorPedidos:

    def __init__(self):
        self.dicionario = {}
        base_dir = Path(__file__).parent
        self.arquivo1 = base_dir / "pedidos.txt"
        self.arquivo2 = base_dir / "pedidos_validos.json"
        self.arquivo3 = base_dir / "erros.log"
        self.arquivo4 = (
            base_dir / "resumo.txt"
        )  # Gera um resumo com quantidades de registros válidos, inválidos e valor total.
        self.processar_pedidos()
        self.salvar_resumo()
    def salvar_log(self,dados):
                with open(self.arquivo3, "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"{dados}\n")


                

    def processar_pedidos(self):
        if not self.arquivo1.exists():
            print("O arquivo nao existe!")
        else:
            with open(self.arquivo1, "r", encoding="utf-8") as a1:
                for linha in a1:
                    linha = linha.strip()
                    if not linha:
                        continue
                    if ";" in linha:
                        pedaco = linha.split(";")
                        if len(pedaco) == 6:
                            (
                                codigo_str,
                                cliente,
                                email,
                                produto,
                                qtd_str,
                                preco_str,
                            ) = pedaco
                            try:
                                codigo = int(codigo_str)
                                quantidade = int(qtd_str)
                                preco_unit = float(preco_str)
                            except ValueError:
                                    erro=(f"Registro inválido: {linha}")
                                    self.salvar_log(erro)
                            except Exception as e:
                                erro2=(e)
                                self.salvar_log(erro2)

                            objs = Pedido(
                                codigo,
                                cliente,
                                produto,
                                email,
                                quantidade,
                                preco_unit,
                            )
                            self.dicionario[codigo] = objs

    def printar(self):
        for i, j in self.dicionario.items():
            print(
                f"Lista de contatos : ",
                j.codigo,
                j.cliente,
                j.email,
                j.produto,
                j.quantidade,
                j.preco_unit,
            )

    def salvar_resumo(self):
         try:
            with open(self.arquivo1,"r",encoding="utf-8")as dados:
                with open(self.arquivo4,"w",encoding="utf-8")as resumo:
                    with open(self.arquivo3,"r",encoding="utf-8")as erros:
                        resumo.write(dados.read())
                        resumo.write(erros.read())
         except Exception as e:
             self.salvar_log(e)




if __name__ == "__main__":
    dados = ImportadorPedidos()
    dados.printar()
