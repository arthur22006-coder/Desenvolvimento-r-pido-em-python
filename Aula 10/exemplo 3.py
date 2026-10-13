def atualizar_pessoa(self, pessoa: Pessoa) -> None:
    conn = self._obter_conexao()
    try:
        with conn:
            conn.execute(
                """UPDATE Pessoa 
                SET 
                    nome = ?,
                    nascimento =  ?,
                    oculos = ?
                WHERE cpf = ? """,
                (
                    pessoa.cpf,
                    pessoa.nome,
                    pessoa.nascimento.isoformat(),
                    int(pessoa.oculos),
                ),
            )
        if cursor.rowcount == 0:
            logger.warning(
                "Nenhuma pessoa encontrad com CPF %s.",
                pessoa.cpf,
            )
            return

        logger.info(
            "Pessoa %s atualizada com sucesso.",
            pessoa.cpf,
        )

    except sqlite3.Error:
        logger.exception(
            "Erro ao inserir pessoa %s.",
            pessoa.cpf,
        )
        raise