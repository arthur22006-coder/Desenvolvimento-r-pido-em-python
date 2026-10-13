def adicionar_coluna_motor(self) -> None:
    conn = self._obter_conexao()

    try:
        colunas = conn.execute(
            "PRAGMA table_info(Veiculo)"
        ).fetchall()

        nomes_colunas = {
            coluna["name"]
            for coluna in colunas
        }

        if "motor" in nomes_colunas:
            logger.info(
                "A coluna 'motor' já existe na tabela Veiculo."
            )
            return

        with conn:
            conn.execute(
                """
                ALTER TABLE Veiculo
                ADD COLUMN motor TEXT
                """
            )

        logger.info(
            "Coluna 'motor' adicionada com sucesso."
        )

    except sqlite3.Error:
        logger.exception(
            "Erro ao adicionar coluna à tabela Veiculo."
        )
        raise