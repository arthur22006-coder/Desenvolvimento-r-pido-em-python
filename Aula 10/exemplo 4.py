def atualizar_pessoa_campos(self, cpf: str, **campos: Any,) ->None:
    conn = self._obter_conexao()

    if not campos:
        raise ValueError("Informe pelo menos um campo para atualizar.")
    campos_invalidos = (set(campos) - self.CAMPOS_PESSOA_PERMITIDOS)

    if campos_invalidos:
        raise ValueError(
            "Campos não permitidos: "
            +",".join(sorted(campos_invalidos))
        )
    atribuicoes: list[str] = []
    valores: list[any] = []
    for nome_campo, valor in campos.itens():
        atribuicoes.append(f"{nome_campo} = ?")
        if nome_campo == "nascimento":
            valor = valor.isoformat()
        elif nome_campo == "oculos":
            valor = int(valor)
        valores.append(valor)
    valores.append(cpf)
    sql = f"""UPDATE Pessoa SET {",".join(atribuicoes)}WHERE cpf = ?"""
    try:
        with conn:
            cursor - conn.execute(sql, tuple(valores),)
        if cursor.rowcount == 0:
            logger.warning("Pessoa %s não encontrada.", cpf,)
            return
    
        logger.info("Pessoa %s atualizada com sucesso.", cpf,)
    except sqlite3.Error:
        logger.exception("Erro ao atalizar pessoa %s.", cpf,)
        raise