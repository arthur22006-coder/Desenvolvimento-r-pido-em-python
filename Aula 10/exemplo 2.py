def inserir_pessoa(self, pessoa: Pessoa) -> None:
    conn = self._obter_conexao()

    try:
        with conn:
            conn.execute(
                """
                INSERT INTO Pessoa (
                    cpf,
                    nome,
                    nascimento,
                    oculos
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    pessoa.cpf,
                    pessoa.nome,
                    pessoa.nascimento.isoformat(),
                    int(pessoa.oculos),
                ),
            )

        logger.info(
            "Pessoa %s inserida com sucesso.",
            pessoa.cpf,
        )

    except sqlite3.IntegrityError:
        logger.exception(
            "Erro de integridade ao inserir pessoa %s.",
            pessoa.cpf,
        )
        raise

    except sqlite3.Error:
        logger.exception(
            "Erro ao inserir pessoa %s.",
            pessoa.cpf,
        )
        raise